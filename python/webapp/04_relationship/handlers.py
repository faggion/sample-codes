# coding: utf8

import os, sys, logging, jinja2, webapp2
#sys.path.insert(0, 'babel.zip')
sys.path.insert(0, 'lib.zip')

from controllers.admin import Tag as AdminTag
from controllers.admin import TagNew as AdminTagNew
from controllers.admin import TaggedArticles as AdminTaggedArticles
from controllers.admin import Article as AdminArticle
from controllers.admin import ArticleNew as AdminArticleNew
from controllers.admin import ArticleDetail as AdminArticleDetail

from controllers.front import Top as FrontTop

class Error(webapp2.RequestHandler):
    def get(self, name):
        self.error(404)
        self.response.out.write(u"404 page not found error template")

app = webapp2.WSGIApplication(
    [
        webapp2.Route(r'/',
                      handler=FrontTop,
                      name="front_top"),

        webapp2.Route(r'/admin/tag/new',
                      handler=AdminTagNew,
                      name="admin_tag_new"),

        webapp2.Route(r'/admin/tag/article',
                      handler=AdminTaggedArticles,
                      name="admin_tagged_articles"),

        webapp2.Route(r'/admin/tag',
                      handler=AdminTag,
                      name="admin_tag"),

        webapp2.Route(r'/admin/article/new',
                      handler=AdminArticleNew,
                      name="admin_article_new"),

        webapp2.Route(r'/admin/article',
                      handler=AdminArticle,
                      name="admin_article"),

        webapp2.Route(r'/admin/article/detail',
                      handler=AdminArticleDetail,
                      name="admin_article_detail"),

        webapp2.Route(r'(.*)', handler=Error),
    ],
    debug=True,
    config={"webapp2_extras.sessions":{'secret_key':'my-super-secret-key'}})

