# coding: utf-8
from flask import make_response
import json

def json_response(body, code=200):
    response = make_response(json.dumps(body), code)
    response.headers['Content-type'] = 'application/json; charset=utf-8'
    return response

