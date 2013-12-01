# coding: utf-8

import datetime
from google.appengine.ext import db
from google.appengine.api import users

class Config(db.Expando):
    vc_sid      = db.StringProperty(required=False)
    yahoo_sid   = db.StringProperty(required=False)
    rakuten_aid = db.StringProperty(required=False)
    amazon_aid  = db.StringProperty(required=False)
    kumapon_aid = db.StringProperty(required=False)

class Advertiser(db.Expando):
    name    = db.StringProperty(required=True)
    expire  = db.IntegerProperty(required=True)
    active  = db.BooleanProperty(required=True)
    score   = db.FloatProperty(required=True)
    fee     = db.IntegerProperty(required=False)
    ratio   = db.FloatProperty(required=False)
    average = db.IntegerProperty(required=False)
    def_vc_pid = db.StringProperty(required=False)

class Creative(db.Expando):
    adv_id    = db.IntegerProperty(required=True)
    name      = db.StringProperty(required=True)
    lp        = db.StringProperty(required=True)
    tmpl_id   = db.IntegerProperty(required=True)
    img_url   = db.StringProperty(required=False)
    title     = db.StringProperty(required=False)
    price     = db.IntegerProperty(required=False)
    org_price = db.IntegerProperty(required=False)
    expire_at = db.IntegerProperty(required=True)

