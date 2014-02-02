# coding: utf-8
from flask import Blueprint, request
import logging, sys, os, traceback
import common, models

app = Blueprint('api_v1_tag', __name__, url_prefix='/api/v1/tag')

@app.route('', methods=['GET'])
def tag_list():
    tags = models.get_keys('Tag')
    ret = []
    for t in tags:
        ret.append(t.id())
    return common.json_response(ret)

@app.route('', methods=['PUT'])
@common.parse_request_body
def tag_create(data):
    num   = int(data.get('num'))
    name  = data.get('name')
    value = data.get('value')
    tag1 = models.Tag.get_key_by_name_and_value(name, value)
    tag2 = models.Tag.get_key_by_num(num)
    if tag1 or tag2:
        return common.error_response(None, 400)

    tag = models.Tag(num=num,
                     name=name,
                     value=value)
    tag.put()
    return common.json_response(tag.format())

@app.route('/<int:tag_id>', methods=['GET'])
def tag_detail(tag_id):
    tag = models.Tag.get_by_id(tag_id)
    if not tag:
        return common.error_response(None, 404)
    return common.json_response(tag.format())

@app.route('/<int:tag_id>', methods=['DELETE'])
def tag_delete(tag_id):
    tag = models.Tag.get_by_id(tag_id)
    if not tag:
        return common.error_response(None, 404)
    tag.delete()
    return common.json_response(body={})

