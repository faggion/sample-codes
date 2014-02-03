# coding: utf-8

import datetime, logging
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext.db import GqlQuery

def get_keys(class_name):
    return GqlQuery('select __key__ from %s order by updated_at desc' % class_name)

class Content(db.Expando):
    title = db.StringProperty(required=True)
    body  = db.TextProperty(required=False)
    tags  = db.ListProperty(db.Key)
    created_at = db.DateTimeProperty(required=False, auto_now_add=True)
    updated_at = db.DateTimeProperty(required=False, auto_now=True)

    def format(self):
        return {"id": self.key().id(),
                "title": self.title,
                "body": self.body,
                "tags": [int(t.id()) for t in self.tags],
                "created_at": self.created_at.isoformat(),
                "updated_at": self.updated_at.isoformat()}

class Tag(db.Expando):
    num   = db.IntegerProperty(required=False)
    name  = db.StringProperty(required=True)
    value = db.StringProperty(required=True)
    parent_tag = db.SelfReferenceProperty(required=False)
    created_at = db.DateTimeProperty(required=False, auto_now_add=True)
    updated_at = db.DateTimeProperty(required=False, auto_now=True)

    @classmethod
    def get_key_by_num(cls, num):
        if not num:
            return None
        sql = 'select __key__ from %s where num = :1' % cls.__name__
        return GqlQuery(sql, num).get()

    @classmethod
    def get_key_by_name_and_value(cls, name, value):
        if not name or not value:
            return None
        sql = 'select __key__ from %s where name = :1 and value = :2' % cls.__name__
        return GqlQuery(sql, name, value).get()

    def format(self):
        return {"id": self.key().id(),
                "num": self.num,
                "name": self.name,
                "value": self.value,
                "created_at": self.created_at.isoformat(),
                "updated_at": self.updated_at.isoformat()}
