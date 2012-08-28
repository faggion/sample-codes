# coding: utf-8
import logging, ConfigParser, os, urllib, string, random, json
from flask import Flask, Response, request, flash, render_template, redirect, url_for, make_response, session
from functools import wraps

app = Flask(__name__)
app.secret_key = 'tanarky'

config = ConfigParser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.password.sample'))

strrange = string.digits + string.letters

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'z' in session and 'name' in session['z']:
            return f(*args, **kwargs)
        return redirect(url_for('login', next=request.url))
    return decorated_function


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/authorize', methods=['GET', 'POST'])
@login_required
def authorize():
    if request.method == 'POST':
        url = request.args.get('redirect_uri', url_for('index'))
        logging.debug(url)
        if request.form.get('approval', 'deny') == 'allow':
            # FIXME: client key/secret 
            params = { 'code': ''.join(random.choice(strrange) for i in xrange(32)),
                       'stage': ''}
        else:
            params = { 'code': '',
                       'state': 'error'}
        return redirect('%s?%s' % (url, urllib.urlencode(params)))

    return render_template('authorize.html')

@app.route('/access_token', methods=['POST'])
def access_token():
    token = ''.join(random.choice(strrange) for i in xrange(32))
    body = json.dumps({"access_token":token,
                       "token_type": "bearer"})
    logging.debug(body)
    response = make_response(body)
    response.headers['Content-type'] = 'application/json; charset=utf-8'
    return response

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = config.get('users', request.form['username'])
        if password and request.form['password'] == password:
            flash(u'You were successfully logged in', 'success')
            session['z'] = { 'name': request.form['username'],
                             'password': request.form['password'] }
            next = request.args.get('next', url_for('index'))
            return redirect(next)
        else:
            flash(u'invalid login id or password', 'error')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    flash(u'You were successfully logged OUT', 'info')
    if 'z' in session:
        session.pop('z')
    return redirect(url_for('login'))

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.DEBUG)
    app.run(debug=True, port=8080)
