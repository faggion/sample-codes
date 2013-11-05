# coding: utf-8
# standard modules
import ConfigParser, os, logging, jinja2, webapp2, md5

# appengine modules
from google.appengine.ext import db, blobstore
from google.appengine.api import images

# my modules
from controllers import env
import helpers
from models.toeic800 import Sentence

class Top(webapp2.RequestHandler):
    @helpers.login_required
    def get(self, user):
        data = db.GqlQuery("SELECT * FROM Sentence where rate > 0 ORDER BY rate DESC").fetch(limit=1000)
        logging.info(data)
        t = env.get_template('toeic800_my_sentences.html')
        tvars = {"user": user,
                 "sentences": data,
                 "name":'satoshi'}

        return self.response.out.write(t.render(T=tvars))

class New(webapp2.RequestHandler):
    @helpers.login_required
    def get(self, user):
        logging.info(user)
        t = env.get_template('toeic800_add_sentence.html')
        tvars = {"user": user,
                 "name":'satoshi'}
        return self.response.out.write(t.render(T=tvars))

    @helpers.login_required
    def post(self, user):
        logging.info(self.request.get('sentence'))
        logging.info(self.request.get('translation'))
        logging.info(self.request.get('words'))
        logging.info(self.request.get('rate'))

        sentence = self.request.get('sentence')
        new_sentence = Sentence(
            key_name    = md5.new(sentence).hexdigest(),
            body        = sentence,
            translation = self.request.get('translation'),
            words       = self.request.get('words'),
            rate        = int(self.request.get('rate')),
            )
        new_sentence.put()

        return self.redirect(self.request.url)

class Edit(webapp2.RequestHandler):
    @helpers.login_required
    def get(self, user, code):
        data = Sentence.get_by_key_name(code)
        if not data:
            self.redirect("/toeic800/new")

        t = env.get_template('toeic800_edit_sentence.html')
        tvars = {"user": user,
                 "sentence": data,
                 "name":'satoshi'}
        return self.response.out.write(t.render(T=tvars))

    @helpers.login_required
    def post(self, user, code):
        sentence = self.request.get('sentence')
        new_sentence = Sentence(
            key_name    = md5.new(sentence).hexdigest(),
            body        = sentence,
            translation = self.request.get('translation'),
            words       = self.request.get('words'),
            rate        = int(self.request.get('rate')),
            )
        new_sentence.put()

        return self.redirect(self.request.url)
