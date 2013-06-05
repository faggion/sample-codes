# coding: utf-8
import logging
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
def index():
    logging.debug(request.headers)
    return u"こんにちは、世界"

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    app.run(debug=True, port=9999)
