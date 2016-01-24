# coding: utf-8
# standard modules
import logging, functools, os, json, hashlib, datetime

# appengine modules
from google.appengine.api import users, memcache
from google.appengine.ext import db, blobstore
from webapp2_extras import i18n 

# my modules
from controllers import env

def admin_required(f):
    @functools.wraps(f)
    def decorated_function(self, *args, **kwargs):
        user = users.get_current_user()
        if not user:
            self.redirect(users.create_login_url(self.request.url))
        elif not users.is_current_user_admin():
            self.redirect(self.url_for('top'))
            #self.abort(403)
        return f(self, *args, **kwargs)
    return decorated_function 

def login_required(f):
    @functools.wraps(f)
    def decorated_function(self, *args, **kwargs):
        user = get_user(self)
        if not user.get('id'):
            self.redirect(users.create_login_url(self.request.url))
        return f(self, user, *args, **kwargs)
    return decorated_function 

def set_locale(f):
    @functools.wraps(f)
    def decorated_function(self, *args, **kwargs):
        locale = self.request.get('locale', None)
        if not locale:
            locale = detect_locale(self.request.headers["Accept-Language"])
        i18n.get_i18n().set_locale(locale)
        return f(self, *args, **kwargs)
    return decorated_function


# http://cvmlrobotics.blogspot.jp/2012/10/detect-user-language-locale-on-google.html
def parse_accept_language(acceptLanguage):
    languages = acceptLanguage.split(",")
    locale_q_pairs = []

    for language in languages:
        if language.split(";")[0] == language:
            # no q => q = 1
            locale_q_pairs.append((language.strip(), "1"))
        else:
            locale = language.split(";")[0].strip()
            q = language.split(";")[1].split("=")[1]
            locale_q_pairs.append((locale, q))
    return locale_q_pairs

def detect_locale(acceptLanguage):
    defaultLocale = 'en_US'
    supportedLocales = ['en_US', 'ja_JP']

    locale_q_pairs = parse_accept_language(acceptLanguage)
    for pair in locale_q_pairs:
        for locale in supportedLocales:
            # pair[0] is locale, pair[1] is q value
            if pair[0].replace('-', '_').lower().startswith(locale.lower()):
                return locale

    return defaultLocale

def get_user(app):
    u = users.get_current_user()
    if u:
        return {"id": u.user_id(),
                "name": u.nickname(),
                "admin": users.is_current_user_admin(),
                "lock_url": "/a/lock/set",
                "logout_url": users.create_logout_url(app.request.uri)}
    else:
        return {"id": None,
                "admin": False,
                "login_url": users.create_login_url(app.request.uri)}
