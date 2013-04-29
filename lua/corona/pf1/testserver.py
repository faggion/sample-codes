# coding: utf-8
import logging
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
def index():
    ret  = u'<h1>this is top page</h1>'
    ret += u'<a href="/">top</a><br>'
    ret += u'<a href="/help">help</a><br>'
    ret += u'<a href="/game">game</a><br>'
    ret += u'<a href="/error">error</a><br>'
    return ret

@app.route('/help', methods=["POST","GET"])
def help():
    ret  = u'<h1>this is help page</h1>'
    ret += u'<a href="/">top</a><br>'
    ret += u'<a href="/help">help</a><br>'
    ret += u'<a href="/game">game</a><br>'
    ret += u'<a href="/error">error</a><br>'
    return ret

@app.route('/game', methods=["POST","GET"])
def game():
    ret  = u'<h1>this is game page</h1>'
    ret += u'<a href="/">top</a><br>'
    ret += u'<a href="/help">help</a><br>'
    ret += u'<a href="/game">game</a><br>'
    ret += u'<a href="/error">error</a><br>'
    return ret

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    app.run(debug=True, port=9999)
