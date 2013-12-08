# coding: utf-8
import logging, sys, os, traceback, json, functools
from flask import request, make_response, redirect, abort
from flask import Blueprint

import tanarky.api.models as models
import tanarky.api.helpers as helpers

cpa_optimizer = Blueprint('cpa_optimizer', __name__)

@cpa_optimizer.errorhandler(404)
def not_found(e):
    r = {'error':{'code': 400000, 'message':'record not found'}}
    return helpers.json_response(r, 404)

@cpa_optimizer.route('/', methods=['GET'])
@helpers.open_session
def index(session):
    ret = helpers.Operator.find_all(models.Media, session)
    logging.info(ret)
    return helpers.json_response(["hello"], 200)

# Adsize
@cpa_optimizer.route('/adsize', methods=['GET'])
@helpers.open_session
def get_adsize_ids(session):
    ads = helpers.Operator.find_all(models.Adsize, session)
    r = []
    for a in ads:
        r.append(a.id)
    return helpers.json_response(r, 200)

@cpa_optimizer.route('/adsize', methods=['POST'])
@helpers.parse_req_body
@helpers.open_session
def post_adsize(session, body):
    _id     = body.get('id')
    _width  = body.get('width')
    _height = body.get('height')
    if not _id or not _width or not _height:
        abort(400)

    a = models.Adsize()
    a.id = _id
    a.width = _width
    a.height = _height
    session.add(a)
    session.commit()
    r = {'id': _id, 'width': _width, 'height': _height}
    return helpers.json_response(r, 200)

@cpa_optimizer.route('/adsize/<int:adsize_id>', methods=['GET'])
@helpers.open_session
def get_adsize_id(session, adsize_id):
    a = helpers.Operator.find_by_id(models.Adsize, session, adsize_id)
    if not a:
        r = {'error':{'code': 400000,
                      'message':'adsize[%d] not found' % adsize_id}}
        return helpers.json_response(r, 404)

    r = {'id': a.id, 'width': a.width, 'height': a.height}
    return helpers.json_response(r, 200)

#@cpa_optimizer.route('/adsize/<int:adsize_id>', methods=['PUT'])
#@helpers.open_session
#def put_adsize_id(session, adsize_id):
#    return helpers.json_response({}, 200)
