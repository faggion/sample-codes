# coding: utf-8
# standard modules
import ConfigParser, os, logging, jinja2, webapp2

# appengine modules
from google.appengine.ext import db, blobstore
from google.appengine.api import images

# my modules
from controllers import env
import helpers

class Top(webapp2.RequestHandler):
    @helpers.login_required
    def get(self, user):
        logging.info(user)
        t = env.get_template('toeic800_my_sentences.html')
        tvars = {"user": user,
                 "name":'satoshi'}
        return self.response.out.write(t.render(T=tvars))
