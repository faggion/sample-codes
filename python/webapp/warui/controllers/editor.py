# coding: utf-8
# standard modules
import ConfigParser, os, logging, jinja2, webapp2

# appengine modules
from google.appengine.ext import db, blobstore
from google.appengine.api import images

# my modules
from controllers import env

class Top(webapp2.RequestHandler):
    def get(self, code):
        t = env.get_template('editor_top.html')
        tvars = {"name":'satoshi'}
        self.response.out.write(t.render(T=tvars))
    def post(self, code):
        self.redirect("/editor/")
