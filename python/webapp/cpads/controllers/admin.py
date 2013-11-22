# coding: utf-8
# standard modules
import ConfigParser, os, logging, jinja2, webapp2, md5

# appengine modules
from google.appengine.ext import db, blobstore
from google.appengine.api import images

# my modules
from controllers import env
import helpers

class Top(webapp2.RequestHandler):
    @helpers.login_required
    def get(self, user):
        t = env.get_template('admin_top.html')
        tvars = {"user": user, "tool": "CPAds"}
        return self.response.out.write(t.render(T=tvars))
