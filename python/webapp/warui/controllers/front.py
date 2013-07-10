# coding: utf-8
# standard modules
import ConfigParser, os, logging, jinja2, webapp2, time, traceback, hashlib
from functools import wraps

# appengine modules
from google.appengine.ext import db, blobstore
from google.appengine.api import images
from google.appengine.api import users

# my modules
from controllers import env
import helpers

from models.room    import Room as mdlRoom
from models.message import Message as mdlMessage

class Top(webapp2.RequestHandler):
    def get(self):
        page  = '<h1>service top</h1>'
        page += '<a href="%s">logout</a></p>' % users.create_logout_url("/")
        page += '<a href="%s">admin</a></p>'  % self.uri_for("admin_top")
        self.response.out.write(page)

class Room(webapp2.RequestHandler):
    def get(self, name):
        t  = env.get_template('room.html')

        messages = db.GqlQuery("select * from Message")

        tv = {"title": "Chat room [%s] " % name,
              "room_name": name,
              "messages": messages,
              "logout": "#",
              "self": self}
        self.response.out.write(t.render(T=tv))

    def post(self, name):
        try:
            room = mdlRoom.get_by_key_name(self.request.POST["room_name"])

            m = mdlMessage(room_name=room.name,
                           icon=int(self.request.POST["icon"]),
                           body=self.request.POST["body"])
            m.put()
        except:
            logging.error(traceback.format_exc())
        time.sleep(1)
        self.redirect("/%s" % name)


