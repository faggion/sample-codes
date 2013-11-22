# coding: utf-8
import logging, sys, os, traceback
from flask import Flask

import models

app = Flask(__name__)
app.secret = 'tanarky'

from controllers.api_v1  import api_v1
app.register_blueprint(api_v1, url_prefix='/adv4/dist/api/1.0')

if __name__ == "__main__":
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)
    app.run(port=5000, host='0.0.0.0', debug=True)
