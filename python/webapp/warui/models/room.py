# coding: utf-8

import datetime
from google.appengine.ext import db
from google.appengine.api import users

class Room(db.Expando):
    name         = db.StringProperty(required=True)
    password     = db.StringProperty(required=True)
    is_active    = db.BooleanProperty(default=True)
    created_at   = db.DateTimeProperty(auto_now_add=True)
    logged_in_at = db.DateTimeProperty()
