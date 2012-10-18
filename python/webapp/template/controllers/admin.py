# coding: utf-8
# standard modules
import ConfigParser, os, logging, jinja2, webapp2
from functools import wraps

# モジュールロード時に実行される部分などはgettext_lazyを使う
from webapp2_extras.i18n import lazy_gettext as _

# appengine modules
from google.appengine.ext import db, blobstore
from google.appengine.api import images
from google.appengine.api import users

# my modules
from controllers import env
import helpers

class AdminBase(webapp2.RequestHandler):
    def template_vars(self, additional):
        tvars = { "tool": u"Admin Tool",
                  "logout": users.create_logout_url(self.request.url) }
        tvars.update(additional)
        return tvars

class Top(AdminBase):
    @helpers.admin_required
    @helpers.set_locale
    def get(self):
        title = _("this is admin top page title here.")
        t  = env.get_template('admin_top.html')
        tv = self.template_vars({"title": title,
                                 "custom": self.uri_for('admin_custom',
                                                        code="foo") })
        self.response.out.write(t.render(T=tv))

    @helpers.admin_required
    def post(self):
        self.redirect("/admin/")

class Custom(AdminBase):
    @helpers.admin_required
    def get(self, code):
        t = env.get_template('admin_custom.html')
        tv = self.template_vars({"title": code,
                                 "code":  code})
        self.response.out.write(t.render(T=tv))

    @helpers.admin_required
    def post(self, code):
        self.redirect("/admin/")

