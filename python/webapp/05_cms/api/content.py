# coding: utf-8
from flask import Blueprint, request
import logging, sys, os, traceback, datetime
import common, models
from google.appengine.ext.db import GqlQuery

app = Blueprint('api_v1_content', __name__, url_prefix='/api/v1/content')

@app.route('', methods=['GET'])
def content_list():
    ret = []
    if request.args.get('rg') == 'large':
        records = models.get_all('Content')
        for t in records:
            ret.append(t.format())
    else:
        records = models.get_keys('Content')
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
    published_at = datetime.datetime.strptime(data.get('published_at'),
                                              '%Y-%m-%dT%H:%M:%S.%f')
    tags   = []
    for t in data.get('tag_nums'):
        k = models.Tag.get_by_num(t)
        if k:
            tags.append(k)

    record = models.Content(title=title,
                            published_at=published_at,
                            body=body,
                            tags=tags)
    if data.get('num'):
        record.num = int(data.get('num'))
    else:
        record.put()
        record.num = record.key().id()

    record.put()
    return common.json_response(record.format())

@app.route('/<int:content_id>', methods=['DELETE'])
def content_delete(content_id):
    record = models.Content.get_by_id(content_id)
    if not record:
        return common.error_response(None, 404)
    record.delete()
    return common.json_response(body={})

