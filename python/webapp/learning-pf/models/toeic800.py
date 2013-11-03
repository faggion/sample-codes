# coding: utf-8

import datetime
from google.appengine.ext import db
from google.appengine.api import users

class Tweet(db.Expando):
    id        = db.IntegerProperty(required=True)
    body      = db.TextProperty(required=True)
    entities  = db.TextProperty()
    posted_at = db.DateTimeProperty(auto_now_add=True)


