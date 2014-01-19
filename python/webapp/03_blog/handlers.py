# coding: utf8

import os, sys, logging, jinja2, webapp2
#sys.path.insert(0, 'babel.zip')
sys.path.insert(0, 'lib.zip')

from controllers.api   import Article as Api_Article
from controllers.api   import ArticleDetail as Api_ArticleDetail
from controllers.admin import Top     as Admin_Top
from controllers.admin import ArticleEditor as Admin_ArticleEditor
from controllers.front import Top     as Front_Top

class Error(webapp2.RequestHandler):
    def get(self, name):
        self.error(404)
        self.response.out.write(u"404 page not found error template")

app = webapp2.WSGIApplication(
    [
        webapp2.Route(r'/',
                      handler=Front_Top,
                      name="front_top"),

        webapp2.Route(r'/api/article/<id:\d+>',
                      handler=Api_ArticleDetail,
                      name="api_article"),

        webapp2.Route(r'/api/article',
                      handler=Api_Article,
                      name="api_article"),


        webapp2.Route(r'/admin/',
                      handler=Admin_Top,
                      name="admin_top"),

        webapp2.Route(r'/admin/edit/(\d+)',
                      handler=Admin_ArticleEditor,
                      name="admin_article_editor"),

        webapp2.Route(r'(.*)', handler=Error),
    ],
    debug=True,
    config={"webapp2_extras.sessions":{'secret_key':'my-super-secret-key'}})

