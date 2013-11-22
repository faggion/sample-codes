# coding: utf8

import os, sys, logging, jinja2, webapp2
sys.path.insert(0, 'babel.zip')

from controllers.front import Top
from controllers.admin import Top as Admin_Top

class Error(webapp2.RequestHandler):
    def get(self, name):
        self.error(404)
        self.response.out.write(u"404 page not found error template")

app = webapp2.WSGIApplication(
    [
        webapp2.Route(r'/admin/', handler=Admin_Top,   name="admin_top"),
        webapp2.Route(r'/',    handler=Top,  name="top"),
        webapp2.Route(r'(.*)', handler=Error),
    ],
    debug=True,
    config={"webapp2_extras.sessions":{'secret_key':'my-super-secret-key'}})

