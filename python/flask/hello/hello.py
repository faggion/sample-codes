# coding: utf-8
#from elixir import Entity, Field, Unicode, Float
from elixir import Field, Unicode, Float
from restful.model import Entity

class Person(Entity):
    name = Field(Unicode)
    age = Field(Float)

#from restful.api import api
from flask import Flask
app = Flask(__name__)
#app.register_module(api, url_prefix='/myrestapi/')

@app.route('/')
def hello_world():
    return u"はろーわーるど1"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
