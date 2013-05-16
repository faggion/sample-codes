# coding: utf-8
from sqlalchemy import create_engine,text,exc
import logging, functools, logging, traceback
from helpers import response_ok, response_error, catch_exception, check_type_request_args, parse_request_body
from errors  import ERROR_MESSAGE
from flask   import Flask, make_response, request, Blueprint

user = Blueprint('user', __name__)

"""
API entriesには必要ないもの
"""
import models
def with_transaction(f):
    @functools.wraps(f)
    def decorated_func(*args, **kwargs):
        with models.conn.begin() as conn:
            return f(conn, *args, **kwargs)
    return decorated_func

def without_transaction(f):
    @functools.wraps(f)
    def decorated_func(*args, **kwargs):
        return f(models.conn, *args, **kwargs)
    return decorated_func

@user.route("/")
@catch_exception
@without_transaction
def user_list(conn):
    sql = "select id, email, name from user"
    ret = []
    for row in conn.execute(text(sql)):
        ret.append(row[0])
    if not ret:
        return response_error(4040000)
    return response_ok(ret)

@user.route("/<id>")
@catch_exception
@without_transaction
def user_detail(conn, id):
    sql = "select id as i , email as e , name as n from user where id = :id limit 1"
    ret = {}
    for row in conn.execute(text(sql), id=id):
        ret = {"id": row.i, "email": row.e, "name": row.n}
    if not ret:
        return response_error(4040000)
    return response_ok(ret)

@user.route("/create")
@catch_exception
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
            return response_error(4000002)
        return response_error(5000000)
    return response_ok({})

