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

class APIBase(webapp2.RequestHandler):
    def json_response(self, body, http_status=200):
        if http_status != 200:
            self.error(http_status)
        self.response.headers['Content-type'] = 'application/json; charset=utf-8'
        return self.response.out.write(json.dumps(body))

#class Lookup(webapp2.RequestHandler):
class Lookup(APIBase):
    def get(self):
        # FIXME: 本当はmedia idでフィルタするべき
        advs = db.Query(models.Advertiser).fetch(100)
        adv_id = None
        adv_est = 0
        for adv in advs:
            adv_est_tmp = adv.ratio * adv.average * 0.01
            logging.error("adv_id: %s, adv_estimatin: %s" % (adv.key().id(), adv_est_tmp))
            if adv_est < adv_est_tmp:
                adv_id = adv.key().id()
        logging.error("adv fixed: %s" % adv_id)

        adcs = db.GqlQuery('select * from Adcreative where adv_id = :adv_id', adv_id=adv_id).run(limit=100)
        for adc in adcs:
            logging.error('"%s"' % adc.adv_id)
        body = {"status":"OK"}
        return self.json_response(body)


