# coding: utf-8
import os, logging
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    logging.error(os.environ.get('ENV_TANARKY_FOO', "no value in env:1"))
    logging.error(os.environ.get('ENV_TANARKY_BAZ', "no value in env:2"))
    return u"ハローワールド"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
