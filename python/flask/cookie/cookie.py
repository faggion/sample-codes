# coding: utf-8
import logging
from flask import Flask, Response, request, flash, render_template, redirect, url_for, make_response

app = Flask(__name__)
app.secret_key = 'tanarky'

@app.route('/')
def index():
    username  = request.cookies.get('username', 'guest name')
    testcookie = request.cookies.get('testcookie', 'no test cookie')
    return render_template('index.html', foo=username, test=testcookie)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            resp = make_response(redirect(url_for('index')))
            resp.set_cookie('username', value='my user name hogehoge2')

            resp.set_cookie('testcookie',
                            value='subdomaincookie',
                            domain='test.tanarky.com')

            resp.set_cookie('testcookie',
                            value='subsubdomaincookie',
                            domain='sub.test.tanarky.com')

            return resp
    return render_template('form.html', error=error)

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.DEBUG)
    app.run(debug=True, port=8080)

"""

Cookie: username="my user name hogehoge2"; testcookie=subsubdomaincookie; testcookie=subdomaincookie

"""
