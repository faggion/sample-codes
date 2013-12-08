# coding: utf-8

from flask import Flask
from tanarky.api.controllers.cpa_optimizer import cpa_optimizer
import tanarky.api.helpers

app = Flask(__name__)
app.secret_key = 'tanarky'

@app.errorhandler(500)
def server_error(e):
    r = {'error':{'code': 500000, 'message':'server error'}}
    return tanarky.api.helpers.json_response(r, 500)

app.register_blueprint(cpa_optimizer, url_prefix='/cpaopt')
