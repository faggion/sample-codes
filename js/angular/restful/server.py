# coding: utf-8
import logging, os, sys, traceback
import json
from flask import Flask, request, make_response, render_template

app = Flask(__name__)

def respond_json(obj, status=200):
    rsp = make_response(json.dumps(obj), status)
    rsp.headers['Content-type'] = 'application/json; charset=utf-8'
    return rsp

@app.route('/tool/user.html')
def tool_user():
    return render_template('user.html')

@app.route('/api/v1/user/<int:_id>', methods=['GET'])
def api_v1_user_detail_get(_id):
    return respond_json({"method": "get", "id": _id})

@app.route('/api/v1/user/<int:_id>', methods=['PUT'])
def api_v1_user_detail_put(_id):
    logging.debug(request.data)
    return respond_json({"method": "put", "id": _id})

@app.route('/api/v1/user', methods=['GET'])
def api_v1_user_list_get():
    return respond_json([ {"id":1},
                          {"id":2},
                          {"id":3} ])

@app.route('/api/v1/user', methods=['POST'])
def api_v1_user_post():
    logging.debug(request.data)
    return respond_json({"method": "post"})

@app.route('/api/v1/user', methods=['DELETE'])
def api_v1_user_delete():
    return respond_json({"method": "delete"})

@app.route('/api/v1/user', methods=['PUT'])
def api_v1_user_put():
    logging.debug(request.data)
    return respond_json({"method": "put"})

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    app.run(debug=True, port=9999)
