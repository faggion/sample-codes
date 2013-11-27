# coding: utf-8
# standard modules
import ConfigParser, os, logging, jinja2, webapp2, md5

# appengine modules
from google.appengine.ext import db, blobstore
from google.appengine.api import images

# my modules
from controllers import env
import helpers
import models

class Top(webapp2.RequestHandler):
    @helpers.admin_required
    def get(self, user):
        advs = db.Query(models.Advertiser).filter('user_id =', user['id'] ).fetch(100)
        logging.error(advs)
        t = env.get_template('admin_top.html')
        tvars = {"user": user, "advs": advs, "self":self}
        return self.response.out.write(t.render(T=tvars))

class Edit(webapp2.RequestHandler):
    @helpers.admin_required
    def get(self, user, adv_id):
        adv = models.Advertiser.get_by_id(int(adv_id))
        t = env.get_template('admin_adv_form.html')
        tvars = {"user": user, "self":self}
        return self.response.out.write(t.render(T=tvars,
                                                name=adv.name,
                                                ratio=adv.ratio,
                                                expire=adv.expire,
                                                average=adv.average,
                                                vc_pid=adv.vc_pid))
    @helpers.admin_required
    def post(self, user, adv_id):
        adv = models.Advertiser.get_by_id(int(adv_id))
        adv.name    = self.request.get('name')
        adv.ratio   = int(self.request.get('ratio'))
        adv.expire  = int(self.request.get('expire'))
        adv.average = int(self.request.get('average'))
        adv.vc_pid  = self.request.get('vc_pid', "")
        adv.put()
        return self.redirect(self.url_for('admin_adv_edit', adv_id=adv_id))

class New(webapp2.RequestHandler):
    @helpers.admin_required
    def get(self, user):
        t = env.get_template('admin_adv_form.html')
        tvars = {"user": user, "self":self}
        return self.response.out.write(t.render(T=tvars))
    @helpers.admin_required
    def post(self, user):
        name    = self.request.get('name')
        ratio   = int(self.request.get('ratio'))
        expire  = int(self.request.get('expire'))
        average = int(self.request.get('average'))
        vc_pid  = self.request.get('vc_pid', "")

        adv = models.Advertiser(
            #key_name = user['id'] + "." + name,
            name     = name,
            user_id  = user['id'],
            ratio    = ratio,
            expire   = expire,
            average  = average,
            vc_pid   = vc_pid,
            )
        adv.put()
        return self.redirect(self.url_for('admin_top'))

class CreativeNew(webapp2.RequestHandler):
    @helpers.admin_required
    def get(self, user, adv_id):
        t = env.get_template('admin_adc_form.html')
        tvars = {"user": user, "self":self }
        return self.response.out.write(t.render(T=tvars,
                                                adv_id=adv_id))
    @helpers.admin_required
    def post(self, user, adv_id):
        adc = models.Adcreative(
            adv_id    = adv_id,
            user_id   = user['id'],
            lp        = self.request.get('lp'),
            tmpl_id   = int(self.request.get('tmpl_id')),
            img_url   = self.request.get('img_url'),
            title     = self.request.get('title'),
            price     = int(self.request.get('price')),
            org_price = int(self.request.get('org_price')),
            )
        adc.put()
        return self.redirect(self.url_for('admin_adv_adc_list', adv_id=adv_id))

class CreativeEdit(webapp2.RequestHandler):
    @helpers.admin_required
    def get(self, user, adv_id, adc_id):
        adc = models.Adcreative.get_by_id(int(adc_id))
        logging.error(adc)
        t = env.get_template('admin_adc_form.html')
        tvars = {"user": user, "self":self }
        return self.response.out.write(t.render(T=tvars,
                                                adv_id=adv_id,
                                                adc_lp=adc.lp,
                                                adc_tmpl_id=adc.tmpl_id,
                                                adc_img_url=adc.img_url,
                                                adc_title=adc.title,
                                                adc_price=adc.price,
                                                adc_org_price=adc.org_price))
    @helpers.admin_required
    def post(self, user, adv_id, adc_id):
        adc = models.Adcreative(
            adv_id    = adv_id,
            user_id   = user['id'],
            lp        = self.request.get('lp'),
            tmpl_id   = int(self.request.get('tmpl_id')),
            img_url   = self.request.get('img_url'),
            title     = self.request.get('title'),
            price     = int(self.request.get('price')),
            org_price = int(self.request.get('org_price')),
            )
        adc.put()
        return self.redirect(self.url_for('admin_adv_adc_list', adv_id=adv_id))

class CreativeList(webapp2.RequestHandler):
    @helpers.admin_required
    def get(self, user, adv_id):
        adcs = db.Query(models.Adcreative).filter('adv_id =', adv_id ).fetch(100)
        t = env.get_template('admin_creative_list.html')
        tvars = {"user": user, "adv_id": adv_id, "adcs":adcs, "self":self }
        return self.response.out.write(t.render(T=tvars))

class Conf(webapp2.RequestHandler):
    @helpers.admin_required
    def get(self, user):
        t = env.get_template('admin_conf.html')
        tvars = {"user": user}
        return self.response.out.write(t.render(T=tvars))
    @helpers.admin_required
    def post(self, user):
        vc_sid      = self.request.get('vc_sid')
        yahoo_sid   = self.request.get('yahoo_sid')
        rakuten_aid = self.request.get('rakuten_aid')
        amazon_aid  = self.request.get('amazon_aid')
        kumapon_aid = self.request.get('kumapon_aid')

        conf = models.Config(
            key_name    = user['id'],
            vc_sid      = vc_sid,
            yahoo_sid   = yahoo_sid,
            rakuten_aid = rakuten_aid,
            amazon_aid  = amazon_aid,
            kumapon_aid = kumapon_aid,
            )
        conf.put()
        return self.redirect(self.url_for('admin_conf'))

