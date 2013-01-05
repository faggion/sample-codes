# coding: utf-8
import logging, time, datetime
from flask import Flask, Response, request, flash, render_template
from flask import redirect, url_for, make_response, session
from functools import wraps

app = Flask(__name__)
app.secret_key = 'tanarky'

class User:
    KEY = 'U'

    @classmethod
    def get_name(self):
        if self.KEY in session and 'name' in session[self.KEY]:
            return session[self.KEY]['name']
        else:
            return None

    @classmethod
    def is_login(self):
        if not self.KEY in session:
            logging.debug('no KEY in session')
            return False

        usess = session[self.KEY]

        if not usess['expire']:
            logging.debug('no expire in session[KEY]')
            return False

        now = int(time.mktime(datetime.datetime.now().timetuple()))
        if int(usess['expire']) < now:
            logging.debug('login expired')
            return False

        return True

    @classmethod
    def do_login(self, name, password):
        if name == 'admin' and password == 'secret':
            now = int(time.mktime(datetime.datetime.now().timetuple()))
            session[self.KEY] = {'name': name,
                                 'expire': now + 60*60*24*1}
            return True
        else:
            if self.KEY in session:
                session.pop(self.KEY)
            return False

    @classmethod
    def do_logout(self):
        if self.KEY in session:
            session.pop(self.KEY)
        return True

@app.route('/')
def index():
    username = User.get_name()
    if not username:
        username = 'guest'
    return render_template('index.html', username=username)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if User.is_login():
            return f(*args, **kwargs)
        return redirect(url_for('login', next=request.url))
    return decorated_function

@app.route('/secret')
@login_required
def secret():
    username = User.get_name()
    return '<h1>you are ok: %s</h1>' % username

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if User.do_login(request.form['username'],
                         request.form['password']):
            flash('You were successfully logged in')
            next = request.args.get('next',
                                    url_for('index'))
            return redirect(next)
        else:
            flash('invalid login id or password')
            return redirect(url_for('login'))

    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    User.do_logout()
    flash('You were successfully logged OUT')
    return redirect(url_for('index'))

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.DEBUG)
    app.run(debug=True, port=8080)
