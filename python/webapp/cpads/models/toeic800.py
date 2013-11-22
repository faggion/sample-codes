# coding: utf-8

import datetime
from google.appengine.ext import db
from google.appengine.api import users

class Sentence(db.Expando):
    body        = db.TextProperty(required=True)
    translation = db.TextProperty(required=True)
    words       = db.TextProperty(required=False)
    rate        = db.IntegerProperty(required=True)



