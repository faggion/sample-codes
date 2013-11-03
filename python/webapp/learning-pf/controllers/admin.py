# coding: utf-8
# standard modules
import ConfigParser, os, logging, jinja2, webapp2, time, traceback, hashlib
from functools import wraps

## モジュールロード時に実行される部分などはgettext_lazyを使う
#from webapp2_extras.i18n import lazy_gettext as _
from webapp2_extras.i18n import gettext as _
from webapp2_extras import sessions

# appengine modules
from google.appengine.ext import db, blobstore
from google.appengine.api import images
from google.appengine.api import users

# my modules
from controllers import env
from models.room import Room
import helpers

class AdminBase(webapp2.RequestHandler):
    def set_message(self, message):
        self.session["MSG"] = message
    def get_message(self):
        ret = self.session.get("MSG")
        if ret:
            del self.session["MSG"]
        return ret

    def set_error(self, message):
        self.session["ERR"] = message
    def get_error(self):
        ret = self.session.get("ERR")
        if ret:
            del self.session["ERR"]
        return ret

    def dispatch(self):
        self.SECRET = "tanarky"

        # Get a session store for this request.
        self.session_store = sessions.get_store(request=self.request)

        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()

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

        rooms = db.GqlQuery("select * from Room")
        #logging.error(rooms)

        tv = self.template_vars({"title": title,
                                 "msg": self.get_message(),
                                 "err": self.get_error(),
                                 "self": self,
                                 "rooms": rooms,
                                 "custom": ""})
        self.response.out.write(t.render(T=tv))

    @helpers.admin_required
    def post(self):
        logging.error("form: room_name = %s" % self.request.POST["name"])

        try:
            room = Room.get_by_key_name(self.request.POST["name"])

            if room and self.request.POST.get("action") == "switch_active_status":
                if room.is_active:
                    room.is_active = False
                else:
                    room.is_active = True
                room.put()
                self.set_message("activation switched")
            elif room and self.request.POST.get("action") == "chpass":
                room.password = hashlib.sha1(self.SECRET+self.request.POST["password"]).hexdigest()
                room.put()
                self.set_message("password changed")
            elif not room:
                r = Room(key_name=self.request.POST["name"],
                         name=self.request.POST["name"],
                         password=hashlib.sha1(self.SECRET+self.request.POST["password"]).hexdigest())
                r.put()
                self.set_message("success")
            else:
                self.set_error("room '%s' already exists" % room.name)
        except:
            logging.error(traceback.format_exc())
            self.set_error("error")
        time.sleep(1)
        self.redirect("/admin/")
