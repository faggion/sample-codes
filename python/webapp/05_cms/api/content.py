# coding: utf-8
from flask import Blueprint
import logging, sys, os, traceback
import common, models
from google.appengine.ext.db import GqlQuery

app = Blueprint('api_v1_content', __name__, url_prefix='/api/v1/content')

@app.route('', methods=['GET'])
def content_list():
    records = GqlQuery('select __key__ from Content order by updated_at desc')
    ret = []
    for t in records:
        ret.append(t.id())
    return common.json_response(ret)

@app.route('/<int:content_id>', methods=['GET'])
def content_detail(content_id):
    record = models.Content.get_by_id(content_id)
    if not record:
        return common.error_response(None, 404)
    return common.json_response(record.format())

@app.route('', methods=['PUT'])
@common.parse_request_body
def content_create(data):
    title  = data.get('title')
    body   = data.get('body')
    record = models.Content(title=title, body=body)
    record.put()
    return common.json_response(record.format())

@app.route('/<int:content_id>', methods=['DELETE'])
def content_delete(content_id):
    record = models.Content.get_by_id(content_id)
    if not record:
        return common.error_response(None, 404)
    record.delete()
    return common.json_response(body={})

