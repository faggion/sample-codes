# coding: utf-8
# standard modules
import ConfigParser, os, logging, jinja2, webapp2, md5, json

# appengine modules
#from google.appengine.ext import db, blobstore
#from google.appengine.api import images

# my modules
from controllers import env
import helpers
import models

class APIBase(webapp2.RequestHandler):
    def json_response(self, body, http_status=200):
        if http_status != 200:
            self.error(http_status)
        self.response.headers['Content-type'] = 'application/json; charset=utf-8'
        return self.response.out.write(json.dumps(body))

class ArticleDetail(APIBase):
    def get(self, id):
        logging.info(type(id))
        if id == "3":
            return self.json_response({"method":"get", "error": "id invalid"}, 400)

        return self.json_response({"method":"get", "id": id, "name": 'tanarky'})
    def post(self, id):
        logging.info(self.request.body)
        if id == "3":
            return self.json_response({"method":"get", "error": "id invalid"}, 400)

        return self.json_response({"method":"get", "id": id, "status": "OK", "name": 'tanarky'})

class Article(APIBase):
    def get(self):
        return self.json_response([{'id':1, 'name':'blog1'},
                                   {'id':2, 'name':'blog2'},
                                   {'id':3, 'name':'blog3'}])
    def put(self):
        return self.json_response({"method":"put"})
    def delete(self):
        return self.json_response({"method":"delete"})
    def post(self):
        return self.json_response({"method":"post"})
