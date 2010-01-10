# -*- coding: utf-8 -*-
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class Page(webapp.RequestHandler):
  def get(self):
    # Query Stringにあるfooパラメータの値を取得する
    # fooパラメータが存在しない場合はデフォルト空文字とする
    foo  = self.request.get('foo', '')

    if foo == "":
      self.response.out.write("fooパラメータはありません。残念。")
    else:
      self.response.out.write("fooパラメータは「%s」です" % foo.encode('utf-8'))

class REST(webapp.RequestHandler):
  def get(self):
    self.response.out.write("このURLに対して、PUT/DELETEも受け付けています。")

  def put(self):
    self.response.out.write("PUT Methodを受け付けました")

  def delete(self):
    self.response.out.write("DELETE Methodを受け付けました")

application = webapp.WSGIApplication([('/', Page),('/rest_test', REST)], debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
