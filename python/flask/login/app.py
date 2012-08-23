# coding: utf-8
import logging
from flask import Flask, Response, request, flash, render_template, redirect, url_for, make_response, session
from functools import wraps

app = Flask(__name__)
app.secret_key = 'tanarky'

@app.route('/')
def index():
    username = 'guest name'
    if 'z' in session and 'name' in session['z']:
        username = session['z']['name']
    return render_template('index.html', username=username)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'z' in session and 'name' in session['z']:
            return f(*args, **kwargs)
        return redirect(url_for('login', next=request.url))
    return decorated_function

@app.route('/secret')
@login_required
def secret():
    username = session['z']['name']
    return '<h1>you are ok: %s</h1>' % username

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            flash('invalid login id or password')
            return redirect(url_for('login'))
        else:
            flash('You were successfully logged in')
            session['z'] = { 'name': request.form['username'], 'password': request.form['password'] }
            next = request.args.get('next', url_for('index'))
            return redirect(next)
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    flash('You were successfully logged OUT')
    if 'z' in session:
        session.pop('z')
    return redirect(url_for('index'))

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.DEBUG)
    app.run(debug=True, port=8080)
