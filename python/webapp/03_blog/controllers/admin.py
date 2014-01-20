# coding: utf-8
# standard modules
import ConfigParser, os, logging, jinja2, webapp2, md5

# appengine modules
from google.appengine.ext import db, blobstore
from google.appengine.api import images

# my modules
from controllers import env
import helpers
import models

class Tool(webapp2.RequestHandler):
    @helpers.admin_required
    def get(self, user):
        t = env.get_template('admin_tool.html')
        tvars = {"user": user}
        return self.response.out.write(t.render(T=tvars))










