# coding: utf-8

import logging, sys, os, traceback, datetime, time
import base64
from flask import Flask, request, make_response, Response, render_template

from email.utils import formatdate

app = Flask(__name__)

@app.route('/')
def top():
    return render_template('top.html')

@app.route('/api.json')
def api():
    logging.debug(request.headers)

    name = 'tanarky2'

    now = datetime.datetime.now()
    stamp = time.mktime(now.timetuple()) + 10
    exp = formatdate(timeval=stamp, localtime=False, usegmt=True)
    logging.debug(exp)

    if request.headers.get('If-None-Match') == name:
        resp = Response(status=304)
        resp.headers['Expires'] = exp
        return resp

    resp = make_response('{"name":"%s"}' % name)
    resp.headers['Content-type'] = 'application/json; charset=utf-8'
    resp.headers['ETag'] = name
    resp.headers['Expires'] = exp
    return resp

@app.route('/track.gif')
def track():
    #logging.debug(request.headers)

    if request.headers.get('If-None-Match') == 'abcdefg':
        return Response(status=304)

    response = make_response(base64.b64decode('R0lGODlhAQABAIAAAAUEBAAAACwAAAAAAQABAAACAkQBADs='))
    response.headers['Content-type'] = 'image/gif'
    response.headers['ETag'] = 'abcdefg'
    return response

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    app.run(debug=True)
