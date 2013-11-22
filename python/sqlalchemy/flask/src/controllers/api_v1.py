# coding: utf-8
import logging, sys, os, traceback
from flask import request, render_template, redirect, url_for, flash
from flask import Blueprint
from flask import current_app as app

import helpers, models

api_v1 = Blueprint('api_v1', __name__)

@api_v1.route("/deliver/<code>", methods=['GET'])
def deliver_show(code):
    session = helpers.Session()
    #res     = session.query(models.Space).filter(models.Space.id == 1).one()
    #parent  = int(res.parent)
    #logging.debug(

    #logging.debug("res = %s" % models.Space.find_by_id(session, int(code)))

    #sp = models.Space()
    #sp.id = 2
    #sp.parent = 2
    #session.merge(sp, load=True)
    #session.commit()

    session.close()
    return "Hello World! %s" % code

@api_v1.route("/deliver/create", methods=['POST'])
def deliver_create():
    session = helpers.Session()

    for i in range(1, 5):
        rtb = models.Rtb()
        rtb.id = i
        session.merge(rtb, load=True)

    for i in range(1, 5):
        m = models.Media()
        m.id = i
        m.rate = 10 * i
        m.rtbs.append(models.Rtb.find_by_id(session, i))
        session.merge(m, load=True)

    session.commit()
    return "Hello World! new"

@api_v1.route("/deliver/<code>", methods=['DELETE'])
def deliver_delete(code):
    session = helpers.Session()
    m = models.Media.find_by_id(session, int(code))
    logging.debug(m.rtbs)
    return "Hello World! new"


"""

media: {
  id: 1,
  rtb: [1,2,3],
}


"""
