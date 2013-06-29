# coding: utf-8

import logging
from flask import Flask, request, make_response

app = Flask(__name__)
app.secret_key = 'tanarky'

@app.route('/', methods=['GET', 'POST', 'OPTIONS'])
def index():
    logging.debug(request.headers)
    response = make_response()
    response.data = "this is response"
    response.headers["Access-Control-Allow-Methods"] = "GET,POST,OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "x-foo"
    response.headers["Access-Control-Allow-Origin"]  = "*"
    return response

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    app.run(debug=True, port=5000)
