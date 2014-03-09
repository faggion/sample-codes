# coding: utf-8
from flask import Blueprint, request
import logging, sys, os, traceback
import common, models

app = Blueprint('api_v1_tag', __name__, url_prefix='/api/v1/tag')

@app.route('', methods=['GET'])
def tag_list():
    ret = []
    if request.args.get('rg') == 'large':
        records = models.get_all('Tag')
        for t in records:
            ret.append(t.format())
    else:
        records = models.get_keys('Content')
        for t in records:
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
    logging.error(data)
    num = data.get('num')
    namespace = data.get('namespace')
    value = data.get('value')
    tag1 = models.Tag.get_key_by_namespace_and_value(namespace, value)
    if tag1:
        logging.info('tag1 namespace and value exists')
        return common.error_response(None, 400)

    parent = None
    if data.get('parentNum'):
        parentNum = data.get('parentNum')
        if not isinstance(parent, int):
            logging.error('parentNum must be int type')
            return common.error_response(None, 400)
        parent = models.get_by_num('Tag', parentNum)
        if not parent:
            logging.error('parent_num(%d) not found' % parentNum)
            return common.error_response(None, 400)

    if num:
        num  = int(num)
        tag2 = models.get_by_num('Tag', num)
        if tag2:
            logging.info('tag2 namespace and value exists')
            return common.error_response(None, 400)
        tag = models.Tag(num=num,
                         namespace=namespace,
                         value=value,
                         parent_tag = parent)
    else:
        tag = models.Tag(namespace=namespace,
                         value=value,
                         parent_tag = parent)
        tag.put()
        tag.num = tag.key().id()

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

