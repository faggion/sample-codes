# coding: utf-8

import zmq,sys

ctx = zmq.Context()
sock = ctx.socket(zmq.REQ)
sock.connect(sys.argv[1])
#sock.connect("tcp://127.0.0.1:9999")

sock.send(sys.argv[2])

sock.close()
