import base64
import os


def random_id() -> str:
    return base64.urlsafe_b64encode(os.urandom(6)).decode()
