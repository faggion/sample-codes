# coding: utf-8

from flask import Flask, request
from flaskext.babel import Babel, lazy_gettext, gettext, refresh

app = Flask(__name__)
app.config.from_pyfile('mysettings.cfg')
babel = Babel(app)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['ja', 'ja_JP', 'en'])

@app.route('/')
def hello_world():
    return gettext(u'hello world')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
