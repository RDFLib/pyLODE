from bs4 import BeautifulSoup as Soup

import falcon
import os
import subprocess


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


api = falcon.App()
api.add_route("/lode", DocResource())
