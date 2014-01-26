# coding: utf-8

import datetime
from google.appengine.ext import db
from google.appengine.api import users

class Article(db.Expando):
    title = db.StringProperty(required=True)
    body  = db.TextProperty(required=False)
    tags  = db.ListProperty(db.Key)

class Tag(db.Expando):
    name  = db.StringProperty(required=True)
    value = db.StringProperty(required=True)
