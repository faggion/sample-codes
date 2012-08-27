# coding: utf-8
import logging, ConfigParser, os, urllib, string, random
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
        logging.error(url)
        if request.form.get('approval', 'deny') == 'allow':
            # FIXME: client key/secret 
            params = { 'code': ''.join(random.choice(strrange) for i in xrange(32)),
                       'stage': ''}
        else:
            params = { 'code': '',
                       'state': 'error'}
        return redirect('%s?%s' % (url, urllib.urlencode(params)))

    return render_template('authorize.html')

# ERROR:root:[('redirect_uri', u'http://localhost:8081/login'), ('client_secret', u'cdf6072ba2d623e0b23b287eae815ce1d4171e44'), ('code', u'w2yugpbbY89etsE5cDHTX3AUCmSrlbMe'), ('client_id', u'1bf5f15595a9c9df5b1a'), ('grant_type', u'authorization_code')]
# ERROR:root:[('redirect_uri', u'http://localhost:8081/login'), ('client_secret', u'user1secret'), ('code', u'aKaTyTlTKNxNOIonYXrFluxmeup8vEkU'), ('client_id', u'key1'), ('grant_type', u'authorization_code')]
@app.route('/access_token', methods=['POST'])
def access_token():
    logging.error(request.headers)
    logging.error(request.form.lists())

    # ERROR:root:[('access_token', '15bbc1a01dd3f57f593e93832512e5e6d9da26ad'), ('token_type', 'bearer')]
    token = ''.join(random.choice(strrange) for i in xrange(32))
    body  = urllib.urlencode({"access_token":token,
                              "token_type": "bearer"})
    response = make_response(body)
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
