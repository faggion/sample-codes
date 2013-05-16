# coding: utf-8

# 
#from sqlalchemy import create_engine,text,exc
import functools, traceback, logging, json
from flask          import Flask, make_response, request
from flaskext.babel import Babel

# Mine
from helpers import response_ok, response_error, catch_exception, check_type_request_args, parse_request_body
from errors  import ERROR_MESSAGE

app = Flask(__name__)
babel = Babel(app)
@babel.localeselector
def get_locale():
    locale = request.accept_languages.best_match(['ja', 'ja_JP', 'en'])
    logging.debug("locale: %s" % locale)
    return locale

"""
API entry points
"""
@app.route("/")
def index():
    return "top page"

from controllers.oauth2 import oauth2
app.register_blueprint(oauth2, url_prefix='/oauth2')

from controllers.user import user
app.register_blueprint(user, url_prefix='/user')

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.DEBUG)
    app.run(debug=True)

"""

CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(80) NOT NULL,
  `email` varchar(120) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8

"""
