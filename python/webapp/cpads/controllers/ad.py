# coding: utf-8
# standard modules
import ConfigParser, os, logging, jinja2, webapp2, md5, json

# appengine modules
from google.appengine.ext import db, blobstore
from google.appengine.api import images

# my modules
from controllers import env
import helpers
import models

class AdBase(webapp2.RequestHandler):
    def json_response(self, body, http_status=200):
        if http_status != 200:
            self.error(http_status)
        self.response.headers['Content-type'] = 'application/json; charset=utf-8'
        return self.response.out.write(json.dumps(body))

class Lookup(AdBase):
    def get(self):
        advs = db.Query(models.Advertiser).fetch(2)
        adv_id = None
        adv_est = 0
        for adv in advs:
            adv_est_tmp = adv.ratio * adv.average * 0.01
            if adv_est < adv_est_tmp:
                adv_id = adv.key().id()

        crs = db.Query(models.Creative).filter('adv_id =', int(adv_id)).fetch(100)
        for cr in crs:
            logging.error('"%s"' % cr.title)
        body = {"status":"OK"}
        return self.json_response(body)


