# coding: utf-8

from flask import Flask
from tanarky.api.controllers.cpa_optimizer import cpa_optimizer

app = Flask(__name__)
app.secret_key = 'tanarky'

app.register_blueprint(cpa_optimizer, url_prefix='/cpaopt')
