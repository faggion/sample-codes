# coding: utf-8

import datetime
from google.appengine.ext import db
from google.appengine.api import users

class Article(db.Expando):
    title = db.StringProperty(required=True)
    body  = db.TextProperty(required=False)
    tags  = db.ListProperty(db.Key)
    created_at = db.DateTimeProperty(required=False, auto_now_add=True)
    updated_at = db.DateTimeProperty(required=False, auto_now=True)

class Tag(db.Expando):
    name  = db.StringProperty(required=True)
    value = db.StringProperty(required=True)
    created_at = db.DateTimeProperty(required=False, auto_now_add=True)
    updated_at = db.DateTimeProperty(required=False, auto_now=True)

    def format(self):
        return {"id": self.key().id(),
                "name": self.name,
                "value": self.value,
                "created_at": self.created_at.isoformat(),
                "updated_at": self.updated_at.isoformat()}
