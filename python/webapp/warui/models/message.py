# coding: utf-8

import datetime
from google.appengine.ext import db
from google.appengine.api import users

class Message(db.Expando):
    room_name = db.StringProperty(required=True)
    icon      = db.IntegerProperty(required=True)
    body      = db.TextProperty(required=True)
    is_active = db.BooleanProperty(default=True)
    posted_at = db.DateTimeProperty(auto_now_add=True)
