import falcon
import subprocess


class DocResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        url = req.get_param("url")
        if url is not None:
            cmd = "cd ./bin && ./pylode.sh -u {url} -c true".format(url=url)

            # remove Overview image placeholder, if present
            unprocessed_html = subprocess.check_output(cmd, shell=True)
            unprocessed_html = unprocessed_html.decode().replace(
                '<section id="overview">', '<section id="overview" style="display:none;">').encode()
            resp.body = unprocessed_html

            resp.set_header("Powered-By", "Falcon")
            resp.set_header("content-type", "text/html")
            resp.status = falcon.HTTP_200


api = falcon.API()
api.add_route("/lode", DocResource())
