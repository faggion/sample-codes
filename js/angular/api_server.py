# coding: utf-8

import logging, sys, os, traceback, json
from flask import Flask, request, make_response

app = Flask(__name__)

def json_response(data):
    rsp = make_response(json.dumps(data))
    rsp.headers['Content-type'] = 'application/json; charset=utf-8'
    return rsp

@app.route('/', methods=['GET'])
def index_get():
    return json_response({'method':'GET', 'hoge':12345})

@app.route('/', methods=['POST'])
def index_post():
    return json_response({'method':'POST', 'hoge':12345})

@app.route('/', methods=['PUT'])
def index_put():
    return json_response({'method':'PUT', 'hoge':12345})

@app.route('/', methods=['DELETE'])
def index_delete():
    return json_response({'method':'DELETE', 'hoge':12345})

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    app.run(debug=True)
