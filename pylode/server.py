from bs4 import BeautifulSoup as Soup
import falcon
import os
import subprocess


class InfoResource:
    def on_get(self, req, resp):
        resp.body = """<h3>pyLODE Server</h3>
                        <p>This is <a href=\"https://github.com/rdflib/pyLODE/\">pyLODE</a> online via Falcon.</p>
                        <p>To use this server to document ontologies, supply an ontology RDF file to it via the See <a href=\"/pylode\">/pylode</a> endpoint.</p>
                        <p>For example, to document the PHS ontology, do this:</p>
                        <ul>
                            <li><code>http://localhost:8000/pylode?url=https://linked.data.gov.au/def/phs</code></li>
                        </ul>
                        <p>Note that this server will use <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Content_negotiation">Content Negotiation</a> to try and get an RDF response from the URI supplied so the ontology must be served with the apprpriate Media Type.</p> 
                    """
        resp.set_header("Powered-By", "Falcon")
        resp.set_header("content-type", "text/html")
        resp.status = falcon.HTTP_200


class DocResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        url = req.get_param("url")
        if url is not None:
            cmd = "cd ./bin && ./pylode.sh -u {url} -c true".format(url=url)

            # remove Overview image placeholder, if present
            raw_html = subprocess.check_output(cmd, shell=True)
            processed_html = raw_html.decode().replace(
                '<section id="overview">', '<section id="overview" style="display:none;">')
            soup = Soup(processed_html, features="html.parser")
            if os.getenv('GTAGID') is not None:
                tag = os.getenv('GTAGID')
                title = soup.find('title')
                async_tag = soup.new_tag("script")
                async_tag['async src'] = "https://www.googletagmanager.com/gtag/js?id=%s" % tag
                title.insert_after(async_tag)
                gtag = soup.new_tag('script')
                gtag.string = """window.dataLayer = window.dataLayer || [];\n
                      function gtag(){dataLayer.push(arguments);}\n
                      gtag('js', new Date());\n
                      gtag('config', '%s');\n""" % tag
                async_tag.insert_after(gtag)
            resp.body = soup

            resp.set_header("Powered-By", "Falcon")
            resp.set_header("content-type", "text/html")
            resp.status = falcon.HTTP_200
        else:
            resp.body = "<h3>USER ERROR</h3><p>For this endpoint, you must supply a Query String Argument of <code>url</code>, e.g. <code>/pylode?url={URL_OF_AN_RDF_FILE}</code>.</p>"
            resp.set_header("content-type", "text/html")
            resp.status = falcon.HTTP_400


api = falcon.API()
api.add_route("/", InfoResource())
api.add_route("/pylode", DocResource())
