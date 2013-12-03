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

class Advertiser(APIBase):
    def get(self):
        name = self.request.get('name','').encode('utf-8')
        adv = db.Query(models.Advertiser).filter('name =', name).get()
        body = {"id": adv.id,
                "media_id": adv.media_id,
                "name": adv.name,
                "expire": adv.expire,
                "active": adv.active,
                "average": adv.average,
                "ratio": adv.ratio,
                "score": adv.score,
                "vc_pid": adv.vc_pid}
        return self.json_response(body)

    def put(self):
        req = json.loads(self.request.body)
        adv = db.Query(models.Advertiser).filter('id =', req['id']).get()
        if not adv:
            adv = models.Advertiser(
                name     = req['name'].encode('utf-8'),
                id       = req['id'],
                media_id = req['media_id'],
                score    = req['score'],
                active   = req['active'],
                ratio    = req['ratio'],
                expire   = req['expire'],
                average  = req['average'],
                vc_pid   = req['vc_pid'])
        else:
            adv.name    = req['name'].encode('utf-8')
            adv.media_id= req['media_id'],
            adv.score   = req['score']
            adv.active  = req['active']
            adv.ratio   = req['ratio']
            adv.expire  = req['expire']
            adv.average = req['average']
            adv.vc_pid  = req['vc_pid']
        
        adv.put()
        body = {}
        return self.json_response(body)

class Creative(APIBase):
    def get(self):
        cr = db.Query(models.Creative).filter('id =', int(self.request.get('id', 0))).get()
        if not cr:
            body = {"error":{"message":"not found"}}
            return self.json_response(body, 404)

        body = {"name": cr.name,
                "adv_id": cr.adv_id,
                "expire_at": cr.expire_at,
                "lp": cr.lp,
                "img_url": cr.img_url,
                "tmpl_id": cr.tmpl_id,
                "title": cr.title,
                "price": cr.price,
                "adv_id": cr.adv_id,
                "org_price": cr.org_price}
        return self.json_response(body)

    def put(self):
        req = json.loads(self.request.body)
        adv = db.Query(models.Advertiser).filter('id =', req['adv_id']).get()
        if not adv:
            body = {"error":{"message":"advertiser not found"}}
            return self.json_response(body, 404)

        cr_name = req['name'].encode('utf-8')
        cr = db.Query(models.Creative).filter('name =', cr_name).get()
        if not cr:
            cr = models.Creative(
                adv_id    = adv.id,
                name      = req['name'],
                tmpl_id   = req['tmpl_id'],
                expire_at = req['expire_at'],
                lp        = req['lp'],
                img_url   = req['img_url'],
                title     = req['title'],
                price     = req['price'],
                org_price = req['org_price'])
        else:
            cr.tmpl_id   = req['tmpl_id']
            cr.expire_at = req['expire_at']
            cr.lp        = req['lp']
            cr.img_url   = req['img_url']
            cr.title     = req['title']
            cr.price     = req['price']
            cr.org_price = req['org_price']

        cr.put()

        body = {}
        return self.json_response(body)
