# coding: utf-8
from sqlalchemy import create_engine,text,exc

import functools, traceback, logging, json
from flask import Flask, make_response, request
app = Flask(__name__)

import models

def response_ok(body):
    if not body.get('code'):
        body["code"] = 2000000
    return json_response(body=body, code=200)

def response_not_found(body):
    return json_response(body=body, code=404)

def response_bad_request(body):
    return json_response(body=body, code=400)

def response_internal_server_error():
    return json_response({"code":5000000, "message":"unexpected error occured"}, code=500)

def json_response(body, code=200):
    response = make_response(json.dumps(body), code)
    response.headers['Content-type'] = 'application/json; charset=utf-8'
    return response

def with_transaction(f):
    @functools.wraps(f)
    def decorated_func(*args, **kwargs):
        with models.conn.begin() as conn:
            try:
                # pass the connection to controller
                return f(conn, *args, **kwargs)
            except:
                # unexpected error occured
                logging.error(traceback.format_exc())
                return response_internal_server_error()
    return decorated_func

def with_no_transaction(f):
    @functools.wraps(f)
    def decorated_func(*args, **kwargs):
        try:
            # pass the connection to controller
            return f(models.conn, *args, **kwargs)
        except:
            # unexpected error occured
            logging.error(traceback.format_exc())
            return response_internal_server_error()

    return decorated_func

@app.route("/")
def index():
    return "ok"

@app.route("/user")
@with_no_transaction
def user_list(conn):
    sql = "select id, email, name from user"
    ret = []
    for row in conn.execute(text(sql)):
        ret.append(row[0])
    if not ret:
        return response_not_found({"code": 4040000,
                                   "message":"no users"})
    return response_ok(ret)

@app.route("/user/<id>")
@with_no_transaction
def user_detail(conn, id):
    sql = "select id as i , email as e , name as n from user where id = :id limit 1"
    ret = {}
    for row in conn.execute(text(sql), id=id):
        ret = {"id": row.i, "email": row.e, "name": row.n}
    if not ret:
        return response_not_found({"code": 4040000,
                                   "message":"user not found: %s" % id })
    return response_ok(ret)

@app.route("/user/create")
@with_transaction
def user_create(conn):
    name  = request.args.get('name')
    email = request.args.get('email')
    sql   = "insert into user set name=:name, email=:email"
    try:
        res = conn.execute(text(sql), name=name, email=email)
    except exc.IntegrityError as ei:
        #logging.error(ei.statement)
        #logging.error(ei.params)
        logging.error(ei.orig[0]) # mysql error code
        logging.error(ei.orig[1]) # mysql error message
        if ei.orig[0] == 1062:
            return response_bad_request({"code":4000001,
                                         "message":"email(%s) already exists" % email})
        raise Exception('unexpected mysql error occured')
    return response_ok({"message":"ok"})

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.DEBUG)
    app.run(debug=True)

"""

CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(80) NOT NULL,
  `email` varchar(120) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8

"""
