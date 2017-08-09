from typing import List

import certifi
import urllib3
from flask import Flask, render_template, json


class Route:
    path = None
    f = None

    def __init__(self, path: str, template: str, ctx_path: str = None):
        def __f():
            if ctx_path is None:
                return render_template(template)
            else:
                http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',
                                           ca_certs=certifi.where())
                ctx = json.loads(http.request('GET', ctx_path).data)

                return render_template(template, context=ctx)

        self.path = path
        self.f = __f


def start(__name__, routes: List[Route], host: str):
    app = Flask(__name__)
    for route in routes:
        app.add_url_rule(route.path, host, route.f)
    app.run(host=host)
