# coding: utf-8
# standard modules
import ConfigParser, os, logging, jinja2, webapp2, time, traceback, hashlib, datetime, json, pytz
from functools import wraps

# appengine modules
from google.appengine.ext import db, blobstore
from google.appengine.api import images, users, memcache, mail

# my modules
from controllers import env
import helpers
import helpers.message

class Top(webapp2.RequestHandler):
    def get(self):
        t = env.get_template('front_top.html')
        tv = {"user": helpers.get_user(self)}
        return self.response.out.write(t.render(T=tv))

