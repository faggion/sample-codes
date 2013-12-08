# coding: utf-8
import logging, functools, json, traceback
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from flask import request, make_response

engine  = create_engine('sqlite:////tmp/cpaopt.sqlite', encoding="utf-8", pool_recycle=60)
Session = sessionmaker(bind=engine)

import tanarky.api.models

class Operator(object):
    @classmethod
    def find_all(cls, model, session):
        return session.query(model).all()

    @classmethod
    def find_by_id(cls, model, session, _id):
        try:
            return session.query(model).filter(model.id == _id).one()
        except NoResultFound, e:
            return None
        except:
            logging.error(traceback.format_exc())
            raise

    @classmethod
    def find_adsize_by_size(cls, session, width, height):
        a = tanarky.api.models.Adsize
        try:
            return session.query(a).filter(a.width == width).filter(a.height == height).one()
        except NoResultFound, e:
            return None
        except:
            logging.error(traceback.format_exc())
            raise

def open_session(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        session = Session()
        ret = f(session, *args, **kwargs)
        session.close()
        return ret
    return decorated_function

def parse_req_body(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        body = json.loads(request.data)
        return f(body, *args, **kwargs)
    return decorated_function

def json_response(obj, status=200):
    response = make_response(json.dumps(obj), status)
    response.headers['Content-type'] = 'application/json; charset=utf-8'
    return response
