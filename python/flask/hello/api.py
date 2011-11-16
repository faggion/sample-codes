# coding: utf-8
from restful.api import api
from flask import Flask

app = Flask(__name__)
app.register_module(api, url_prefix='/myrestapi/')
