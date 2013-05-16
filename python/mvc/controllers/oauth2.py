# coding: utf-8
import logging, traceback
from helpers import response_ok, response_error, catch_exception, check_type_request_args, parse_request_body
from errors  import ERROR_MESSAGE
from flask   import Flask, make_response, request, Blueprint, render_template

oauth2 = Blueprint('oauth2', __name__)

@oauth2.route("/authz", methods=["GET"])
@catch_exception
@check_type_request_args(required=[(str, "response_type"),
                                   (int, "client_id"),
                                   (str, "scope")],
                         optional=[(str, "redirect_uri", None)])
def oauth2_authz_get(response_type, client_id, scope, redirect_uri):
    return render_template("oauth2_allow.html")

@oauth2.route("/authz", methods=["POST"])
@catch_exception
@check_type_request_args(required=[(unicode, "response_type"),
                                   (int, "client_id"),
                                   (str, "scope")])
@parse_request_body
def oauth2_authz_post(body, response_type, client_id, scope):
    return response_ok({})

@oauth2.route("/token", methods=["GET", "POST"])
@catch_exception
@check_type_request_args(required=[(int,"client_id")], optional=[(str, "user_id", "default_id")])
@parse_request_body
def oauth2_token(data, client_id, user_id):
    # 厳密なリクエストパラメータチェック(正規表現など)はここでやる
    logging.debug(request.headers)
    logging.debug(data)
    logging.debug(client_id)
    logging.debug(user_id)
    return response_ok({})

