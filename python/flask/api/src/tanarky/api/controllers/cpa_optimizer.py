# coding: utf-8
import logging, sys, os, traceback, json, functools
from flask import request, make_response, redirect
from flask import Blueprint

import tanarky.api.models as models
import tanarky.api.helpers as helpers

cpa_optimizer = Blueprint('cpa_optimizer', __name__)

@cpa_optimizer.route('/', methods=['GET'])
@helpers.open_session
def index(session):
    ret = helpers.Operator.find_all(models.Media, session)
    logging.info(ret)
    return helpers.json_response(["hello"], 200)

# Adsize
@cpa_optimizer.route('/adsize', methods=['GET'])
def get_adsize_ids():
    return helpers.json_response(["adsize ids"], 200)

@cpa_optimizer.route('/adsize', methods=['POST'])
@helpers.open_session
@helpers.parse_req_body
def post_adsize(session, body):
    return helpers.json_response(["create adsize"], 200)

@cpa_optimizer.route('/adsize/<int:adsize_id>', methods=['GET'])
def get_adsize_id(adsize_id):
    return helpers.json_response(["get adsize detail: %d" % adsize_id], 200)

@cpa_optimizer.route('/adsize/<int:adsize_id>', methods=['PUT'])
def put_adsize_id(adsize_id):
    return helpers.json_response(["put adsize"], 200)
