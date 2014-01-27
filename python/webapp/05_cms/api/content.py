# coding: utf-8
from flask import Blueprint
import logging, sys, os, traceback
import common

app = Blueprint('api_v1_content', __name__, url_prefix='/api/v1/content')

@app.route('', methods=['GET'])
def content_list():
    return common.json_response([])

@app.route('/<int:tag_id>', methods=['GET'])
def content_detail(tag_id):
    return common.json_response({"id": tag_id})
