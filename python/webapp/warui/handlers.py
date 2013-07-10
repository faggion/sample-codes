# coding: utf8

import os, sys, logging, jinja2, webapp2
sys.path.insert(0, 'babel.zip')
sys.path.insert(0, 'pytz.zip')

import controllers.editor
import controllers.event
import controllers.admin
import controllers.front

class Error(webapp2.RequestHandler):
    def get(self, name):
        self.error(404)
        self.response.out.write(u"404 page not found error template")



app = webapp2.WSGIApplication(
    [
        # Admin
        webapp2.Route(r'/admin/',       handler=controllers.admin.Top,  name="admin_top"),

        # Frontend Top
        webapp2.Route(r'/<name:\w+>', handler=controllers.front.Room, name='front_room'),
        webapp2.Route(r'/',           handler=controllers.front.Top,  name="top"),
        webapp2.Route(r'(.*)',        handler=Error),
    ],
    debug=True,
    config={"webapp2_extras.sessions":{'secret_key':'my-super-secret-key'}})

#logging.getLogger().setLevel(logging.DEBUG)
