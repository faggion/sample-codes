# coding: utf-8
import logging, os, sys, traceback
from flask import Flask, request
from flaskext.xmlrpc import XMLRPCHandler, Fault

app = Flask(__name__)

handler = XMLRPCHandler('api')
handler.connect(app, '/api')

@handler.register
def ping(name="world"):
    if not name:
        raise Fault("unknown_recipient", "I need someone to greet!")
    return "Hello, %s!" % name

# pip search compatible
@handler.register
def search(params, name):
    logging.error(request.data)
    return [{"name":"foo1", "summary":'bar1', "version":"1.0.0", "_pypi_ordering":0.3},
            {"name":"foo3", "summary":'bar3', "version":"1.3.0", "_pypi_ordering":0.8},
            {"name":"foo2", "summary":'bar2', "version":"2.1.0", "_pypi_ordering":0.2},]

if __name__ == "__main__":
    app.run(debug=True)
