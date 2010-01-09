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

application = webapp.WSGIApplication([('/', Page)], debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
