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
    user_id = db.StringProperty(required=True)
    ratio   = db.IntegerProperty(required=True)
    expire  = db.IntegerProperty(required=True)
    average = db.IntegerProperty(required=True)
    vc_pid  = db.StringProperty(required=False)

class Adcreative(db.Expando):
    adv_id    = db.StringProperty(required=True)
    user_id   = db.StringProperty(required=True)
    lp        = db.StringProperty(required=True)
    tmpl_id   = db.IntegerProperty(required=True)
    img_url   = db.StringProperty(required=False)
    #img_pos_x = db.IntegerProperty(required=False)
    #img_pos_y = db.IntegerProperty(required=False)
    title     = db.StringProperty(required=False)
    price     = db.IntegerProperty(required=False)
    org_price = db.IntegerProperty(required=False)

