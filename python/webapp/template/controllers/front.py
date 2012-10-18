# coding: utf-8
# standard modules
import ConfigParser, os, logging, jinja2, webapp2
from functools import wraps

# appengine modules
from google.appengine.ext import db, blobstore
from google.appengine.api import images
from google.appengine.api import users

# my modules
import helpers

class Top(webapp2.RequestHandler):
    def get(self):
        page  = '<h1>service top</h1>'
        page += '<a href="%s">logout</a></p>' % users.create_logout_url("/")
        page += '<a href="%s">admin</a></p>'  % self.uri_for("admin_top")
        self.response.out.write(page)

