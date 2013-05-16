# coding: utf-8
import logging

# TODO: 多言語化
# TODO: %s を受け取る
def ERROR_MESSAGE(code):
    error_messages = {
        2000000: "OK",
        4000000: "bad request: required params do not exist",
        4000001: "bad request: not allowed methods",
        4000002: "bad request: duplicate email",
        4040000: "not found: no user",
        4040001: "not found: no api",
        4040002: "not found: no event",
        5000000: "internal server error: unexpected error occured 5000000",
        5000001: "internal server error: unexpected error occured 5000001",
        }
    if not error_messages.get(code):
        return error_messages.get(5000000)
    return error_messages.get(code)
