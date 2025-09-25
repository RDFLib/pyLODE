
import logging
import os
import sys

from bs4 import BeautifulSoup as Soup
import falcon
import validators
from wsgiref.simple_server import make_server

from .profiles.ontpub import OntPub
from .profiles.vocpub import VocPub
from .profiles.supermodel.html import Supermodel


# Configure logging before anything else
if __name__ == '__main__':
    # Log configuration should up to this application
    for handler in logging.root.handlers[:]:
        # remove existing handler added by some import somewhere...
        logging.root.removeHandler(handler)
    logging.basicConfig(
        format=f'%(asctime)s.%(msecs)03d %(levelname)s [pid=%(process)d %(threadName)s %(name)s:%(lineno)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=os.getenv('LOG_LEVEL', 'INFO').upper(),
        stream=sys.stdout
    )
elif 'gunicorn.error' in logging.Logger.manager.loggerDict:
    # This application is running under GUnicorn, which has already initialised logging.
    # Ensure pylode server logs are directed to the GUnicorn error log.
    root_logger = logging.getLogger()
    root_logger.setLevel(os.getenv('LOG_LEVEL', 'INFO').upper())
    gunicorn_logger = logging.getLogger('gunicorn.error')
    for gunicorn_handler in gunicorn_logger.handlers:
        root_logger.addHandler(gunicorn_handler)


_logger = logging.getLogger(__name__)


class HtmlResponseCustomiser:
    def process_response(self, req: falcon.Request, resp: falcon.Response, resource: object, req_succeeded: bool) -> None:
        """Post-processing of a Falcon app response (after routing).

        Args:
            req: Request object.
            resp: Response object.
            resource: Resource object to which the request was
                routed. May be None if no route was found
                for the request.
            req_succeeded: True if no exceptions were raised while
                the framework processed and routed the request;
                otherwise False.
        """
        content_type = resp.get_header('content-type', None)
        if content_type is None or content_type == 'text/html':
            # Determine whether any customisation has been required
            css_url = os.getenv('CSS_URL')
            favicon_url = os.getenv('FAVICON_URL')
            gtag_id = os.getenv('GTAGID')
            if css_url or favicon_url or gtag_id:
                # Customisations *have* been configured
                # Modify whatever HTML is currently in the response object
                soup = Soup(resp.text, features='html.parser')
                head = soup.find('head')
                if css_url:
                    _logger.debug('Injecting custom css link')
                    css_tag = soup.new_tag('link')
                    css_tag['rel'] = 'stylesheet'
                    css_tag['href'] = css_url
                    head.append(css_tag)

                if favicon_url:
                    _logger.debug('Injecting custom favicon link')
                    favicon_tag = soup.new_tag('link')
                    favicon_tag['rel'] = 'icon'
                    favicon_tag['type'] = os.getenv('FAVICON_MIME', 'image/x-icon')
                    favicon_tag['href'] = favicon_url
                    head.append(favicon_tag)

                if gtag_id:
                    _logger.debug('Injecting custom google analytics tag')
                    async_tag = soup.new_tag('script')
                    async_tag['async src'] = f'https://www.googletagmanager.com/gtag/js?id={gtag_id}'
                    gtag = soup.new_tag('script')
                    gtag.string = f"""window.dataLayer = window.dataLayer || [];
                        function gtag(){{dataLayer.push(arguments);}}
                        gtag('js', new Date());
                        gtag('config', '{gtag_id}');"""
                    head.append(async_tag)
                    async_tag.insert_after(gtag)
                resp.text = soup.prettify(formatter='html')
                if content_type is None:
                    resp.content_type = 'text/html'
            else:
                _logger.debug('No HTML cutomisations have been configured')
        else:
            _logger.debug(f'Skipping HTML customisations for {content_type} response')


class InfoResource:
    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """Landing page for the pyLODE Web Service."""

        resp.text = """<html>
            <head>
                <title>pyLODE Server</title>
            </head>
            <body>
                <h1>pyLODE Server</h1>
                <p>This is <a href=\"https://github.com/rdflib/pyLODE/\">pyLODE</a> online via Falcon.</p>
                <p>To use this server to document ontologies, supply an ontology RDF file to it via the <a href=\"/pylode\">/pylode</a> endpoint.</p>
                <p>For example, to document the PHS ontology, do this:</p>
                <ul>
                    <li><code>http://localhost:8000/pylode?url=https://linked.data.gov.au/def/phs</code></li>
                </ul>
                <p>Note that this server will use <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Content_negotiation">Content Negotiation</a> to try and get an RDF response from the URI supplied so the ontology must be served with the apprpriate Media Type.</p>
            </body>
        </html>"""
        resp.set_header("content-type", "text/html")
        resp.status = falcon.HTTP_200


class DocResource:
    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """Serves up a pyLODE-converted copy of the RDF document provided by the `url` request parameter"""
        url = req.get_param('url', required=True)
        if not validators.url(url):
            _logger.error(f"Failing pyLODE request for invalid url parameter '{url}'")
            raise falcon.HTTPBadRequest(
                description='`url` parameter value must be a valid absolute URL'
            )
        sort_subjects = req.get_param_as_bool('sort', required=False, blank_as_true=True, default=True)
        profile = req.get_param("profile", required=False, default="ontpub").lower()
        _logger.info(f"Processing pyLODE request for '{profile}' rendering of '{url}' with sort_subjects = {sort_subjects}")
        match profile:
            case "ontpub":
                ontology_doc = OntPub(url, sort_subjects=sort_subjects)
            case "supermodel":
                ontology_doc = Supermodel(url, sort_subjects=sort_subjects)
            case "vocpub":
                ontology_doc = VocPub(url, sort_subjects=sort_subjects)
            case _:
                _logger.error(f"Failing pyLODE request for invalid profile parameter '{profile}'")
                raise falcon.HTTPBadRequest(
                    description='Unrecognised `profile` parameter value'
                )
        resp.text = ontology_doc.make_html(include_css=True)
        resp.set_header("content-type", "text/html")
        resp.status = falcon.HTTP_200


# Initialise the Web Application
api = falcon.App(middleware=[HtmlResponseCustomiser()])
api.add_route("/", InfoResource())
api.add_route("/pylode", DocResource())


if __name__ == '__main__':
    # Launch a standalone HTTP server
    listen_port = int(os.getenv('PORT', 8000))
    with make_server('', listen_port, api) as httpd:
        # Serve until process is killed
        httpd.serve_forever()
