# coding: utf-8
from flask import make_response, request
import logging, os, sys, json, functools

def json_response(body=None, code=200):
    response = make_response(json.dumps(body), code)
    response.headers['Content-type'] = 'application/json; charset=utf-8'
    return response

def error_response(body=None, code=500):
    response = make_response(json.dumps(body), code)
    response.headers['Content-type'] = 'application/json; charset=utf-8'
    return response

def parse_request_body(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        data = json.loads(request.data)
        return f(data, *args, **kwargs)
    return decorated_function 
