#!/usr/bin/env python3
""" Flask Application """

from os import environ
from flask import Flask
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)


if __name__ == "__main__":
    """ Entry Point """
    host = environ.get('MDL_API_HOST')
    port = environ.get('MDL_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)