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

@app.route('/num', methods=['GET'])
def tag_num_list():
    tags = models.get_all('Tag')
    ret = []
    for t in tags:
        ret.append(t.num)
    return common.json_response(ret)

@app.route('', methods=['PUT'])
@common.parse_request_body
def tag_create(data):
    num   = data.get('num')
    name  = data.get('name')
    value = data.get('value')
    tag1  = models.Tag.get_key_by_name_and_value(name, value)
    if tag1:
        return common.error_response(None, 400)

    if num:
        num  = int(num)
        tag2 = models.get_by_num('Tag', num)
        if tag2:
            return common.error_response(None, 400)
        tag = models.Tag(num=num,
                         name=name,
                         value=value,
                         is_end=data.get('is_end'))
    else:
        tag = models.Tag(name=name,
                         value=value,
                         is_end=data.get('is_end'))
        tag.put()
        tag.num = tag.key().id()

    parent = data.get('parent')
    if parent:
        # FIXME: int cast error
        parent_num = int(parent)
        parent = models.get_by_num('Tag', parent_num)
        if not parent:
            logging.error('parent_num(%d) not found' % parent_num)
            return common.error_response(None, 400)
        tag.parent_tag = parent

    tag.put()
    return common.json_response(tag.format())

@app.route('/<int:tag_id>', methods=['GET'])
def tag_detail(tag_id):
    tag = models.Tag.get_by_id(tag_id)
    if not tag:
        return common.error_response(None, 404)
    return common.json_response(tag.format())

@app.route('/num/<int:tag_num>', methods=['GET'])
def tag_detail_by_num(tag_num):
    tag = models.get_by_num('Tag', tag_num, key_only=False)
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

