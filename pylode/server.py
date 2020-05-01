import falcon
import subprocess


class DocResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        url = req.get_param("url")
        if url is not None:
            cmd = "cd ./bin && ./pylode.sh -u {url} -c true".format(url=url)
            resp.body = subprocess.check_output(cmd, shell=True)
            resp.set_header("Powered-By", "Falcon")
            resp.status = falcon.HTTP_200


api = falcon.API()
api.add_route("/lode", DocResource())
