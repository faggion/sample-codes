# -*- coding: utf-8 -*-
import cgi

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from django.utils import simplejson

class MainPage(webapp.RequestHandler):
  def get(self):
    self.response.out.write("""
      <html>
        <body>
          <form action="/sign" method="post">
            <div><textarea name="content" rows="3" cols="60"></textarea></div>
            <div><input type="submit" value="Sign Guestbook"></div>
          </form>
        </body>
      </html>""")


class Guestbook(webapp.RequestHandler):
  def post(self):
      back = "/"
      res  = {}
      user = users.get_current_user()
      if not user:
          res["nickname"] = 'ゲストさん'
          res["login"]    = users.create_login_url(back)
      else:
          res["nickname"] = user.nickname()
          res["user_id"]  = user.user_id()
          res["logout"]   = users.create_logout_url(back)

      self.response.headers['Content-type'] = 'application/json'
      self.response.out.write(simplejson.dumps(res, ensure_ascii=False))
      #self.response.out.write(cgi.escape(self.request.get('content')))

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/sign', Guestbook)],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
