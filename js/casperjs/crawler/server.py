# coding: utf-8
import os, sys, logging
from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/', methods=['GET'])
def index():
    name = request.cookies.get('name')
    logging.debug(request.cookies)
    logging.debug(request.cookies.get('name'))
    if name:
        T = {'name':name}
        return render_template('index.html', T=T)
    return render_template('form.html')

@app.route('/login', methods=['POST'])
def login():
    response = make_response(redirect(url_for('index')))
    response.set_cookie('name', request.form.get('name',''))
    return response

@app.route('/logout', methods=['GET'])
def logout():
    logging.debug(request.headers)
    response = app.make_response(redirect(url_for('index')))
    response.set_cookie('name', '')
    return response

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    app.run(debug=True)
