# coding: utf-8
# standard modules
import ConfigParser, os, logging, jinja2, webapp2, time, traceback, hashlib, dateutil.parser, datetime, json, pytz
from functools import wraps

# appengine modules
from google.appengine.ext import db, blobstore
from google.appengine.api import images, users, memcache, mail

# my modules
from controllers import env
import helpers
import helpers.message

TZ = dateutil.tz.gettz('Asia/Tokyo')

class Top(webapp2.RequestHandler):
    def get(self):
        # user check
        user = helpers.get_user(self)
        if not user.get('id'):
            tv = {"user": user}
            t = env.get_template('login.html')
            return self.response.out.write(t.render(T=tv))

        t = env.get_template('menu.html')
        tv = {"user": user}
        return self.response.out.write(t.render(T=tv))

