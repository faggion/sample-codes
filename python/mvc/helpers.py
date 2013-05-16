# coding: utf-8

import functools, logging, traceback, json
from flask import Flask, make_response, request

from errors  import ERROR_MESSAGE

def response_ok(body):
    return response_json(api_status=2000000, body=body)

def response_error(api_status):
    return response_json(api_status=api_status)

def response_json(api_status, body=None):
    api_status_message = ERROR_MESSAGE(api_status)
    http_status = int(str(api_status)[0:3])
    results = { "header": { "code": api_status, "message": api_status_message} }
    if body:
        results["body"] = body
    response = make_response(json.dumps(results), http_status)
    response.headers['Content-type'] = 'application/json; charset=utf-8'
    return response

def catch_exception(f):
    @functools.wraps(f)
    def decorated_func(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except:
            logging.error(traceback.format_exc())
            return response_error(5000000)
    return decorated_func
def check_type_request_args(required=[], optional=[]):
    def wrapper1(f):
        @functools.wraps(f)
        def wrapper2():
            params = {}
            for t in required + optional:
                default = t[2] if len(t) == 3 else None
                raw_val = request.args.get(t[1], default)
                if len(t) == 2 and not raw_val:
                    return response_error(4000000)
                try:
                    params[t[1]] = t[0](raw_val)
                except:
                    return response_error(4000000)
            return f(**params)
        return wrapper2
    return wrapper1
def parse_request_body(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        try:
            if request.method == "GET":
                return f(None, **kwargs)
            return f({"foo":"bar"}, *args, **kwargs)
        except:
            logging.error(traceback.format_exc())
            return response_error(5000000)
    return wrapper
