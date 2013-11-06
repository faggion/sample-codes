# coding: utf8

import os, sys, logging, jinja2, webapp2
sys.path.insert(0, 'babel.zip')

from controllers.front    import Top
from controllers.toeic800 import Top  as Toeic800_Top
from controllers.toeic800 import New  as Toeic800_New
from controllers.toeic800 import Edit as Toeic800_Edit
from controllers.toeic800 import Rate as Toeic800_Rate

class Error(webapp2.RequestHandler):
    def get(self, name):
        self.error(404)
        self.response.out.write(u"404 page not found error template")

app = webapp2.WSGIApplication(
    [
        webapp2.Route(r'/toeic800/',    handler=Toeic800_Top,  name="toeic800_top"),
        webapp2.Route(r'/toeic800/new', handler=Toeic800_New,  name="toeic800_new"),
        webapp2.Route(r'/toeic800/<code:\w+>/rate/<point:\d+>', handler=Toeic800_Rate, name="toeic800_rate"),
        webapp2.Route(r'/toeic800/<code:\w+>/edit', handler=Toeic800_Edit, name="toeic800_edit"),
        webapp2.Route(r'/',    handler=Top,  name="top"),
        webapp2.Route(r'(.*)', handler=Error),
    ],
    debug=True,
    config={"webapp2_extras.sessions":{'secret_key':'my-super-secret-key'}})

