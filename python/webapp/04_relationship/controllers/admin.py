# coding: utf-8
# standard modules
import ConfigParser, os, logging, jinja2, webapp2, md5, time

# appengine modules
from google.appengine.ext import db, blobstore
from google.appengine.api import images, memcache

# my modules
from controllers import env
import helpers
import models

class Tag(webapp2.RequestHandler):
    @helpers.admin_required
    def get(self, user):
        tags = models.Tag.all().order('-updated_at').fetch(limit=1000)
        t = env.get_template('admin_tag.html')
        tvars = {"user":user, "tags":tags}
        return self.response.out.write(t.render(T=tvars))

class TagNew(webapp2.RequestHandler):
    @helpers.admin_required
    def get(self, user):
        t = env.get_template('admin_tag_new.html')
        tvars = {"user": user}
        return self.response.out.write(t.render(T=tvars))

    @helpers.admin_required
    def post(self, user):
        name = self.request.get('name')
        value = value=self.request.get('value')
        tag = models.Tag(name=name,
                         value=value)
        tag.put()
        time.sleep(0.10)
        return self.redirect('/admin/tag')

class TaggedArticles(webapp2.RequestHandler):
    @helpers.admin_required
    def get(self, user):
        tag = models.Tag.get_by_id(int(self.request.get("tid")))
        a = models.Article.all().filter('tags =', tag).fetch(100)
        t = env.get_template('admin_tagged_articles.html')
        tvars = {"user": user, "articles": a, "tag": tag}
        return self.response.out.write(t.render(T=tvars))


class Article(webapp2.RequestHandler):
    @helpers.admin_required
    def get(self, user):
        articles = models.Article.all().fetch(limit=1000)
        t = env.get_template('admin_article.html')
        tvars = {"user": user, "articles": articles}
        return self.response.out.write(t.render(T=tvars))

class ArticleNew(webapp2.RequestHandler):
    @helpers.admin_required
    def get(self, user):
        tags = models.Tag.all().fetch(limit=1000)
        t = env.get_template('admin_article_new.html')
        tvars = {"user": user, "tags": tags}
        return self.response.out.write(t.render(T=tvars))

    @helpers.admin_required
    def post(self, user):
        tags = self.request.get_all('tags')
        title = self.request.get('title')
        body = self.request.get('body')
        article = models.Article(title=title, body=body)

        for t in tags:
            article.tags.append(db.Key(encoded=t))

        article.put()
        time.sleep(0.10)
        return self.redirect('/admin/article')

class ArticleDetail(webapp2.RequestHandler):
    @helpers.admin_required
    def get(self, user):
        a = models.Article.get_by_id(int(self.request.get("aid")))
        logging.error(a)
        t = env.get_template('admin_article_detail.html')
        tvars = {"user": user, "article": a, "tags": db.get(a.tags)}
        return self.response.out.write(t.render(T=tvars))

