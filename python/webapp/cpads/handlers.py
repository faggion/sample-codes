# coding: utf8

import os, sys, logging, jinja2, webapp2
sys.path.insert(0, 'babel.zip')

from controllers.front import Top
from controllers.admin import Top  as Admin_Top
from controllers.admin import Conf as Admin_Conf
from controllers.admin import CreativeList as Admin_Adv_CreativeList
from controllers.admin import CreativeNew  as Admin_Adv_CreativeNew
from controllers.admin import CreativeEdit as Admin_Adv_CreativeEdit
from controllers.admin import New  as Admin_Adv_New
from controllers.admin import Edit as Admin_Adv_Edit

class Error(webapp2.RequestHandler):
    def get(self, name):
        self.error(404)
        self.response.out.write(u"404 page not found error template")

app = webapp2.WSGIApplication(
    [
        webapp2.Route(r'/admin/conf',
                      handler=Admin_Conf,
                      name="admin_conf"),

        webapp2.Route(r'/admin/adv/new',
                      handler=Admin_Adv_New,
                      name="admin_adv_new"),

        webapp2.Route(r'/admin/adv/<adv_id:\w+>',
                      handler=Admin_Adv_CreativeList,
                      name="admin_adv_adc_list"),

        webapp2.Route(r'/admin/adv/<adv_id:\w+>/edit',
                      handler=Admin_Adv_Edit,
                      name="admin_adv_edit"),

        webapp2.Route(r'/admin/adv/<adv_id:\w+>/adc/new',
                      handler=Admin_Adv_CreativeNew,
                      name="admin_adv_adc_new"),

        webapp2.Route(r'/admin/adv/<adv_id:\w+>/adc/<adc_id:\w+>',
                      handler=Admin_Adv_CreativeEdit,
                      name="admin_adv_adc_edit"),

        webapp2.Route(r'/admin/', handler=Admin_Top,   name="admin_top"),
        webapp2.Route(r'/',    handler=Top,  name="top"),
        webapp2.Route(r'(.*)', handler=Error),
    ],
    debug=True,
    config={"webapp2_extras.sessions":{'secret_key':'my-super-secret-key'}})

