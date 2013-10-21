# coding: utf-8

import zmq,sys

ctx = zmq.Context()
sock = ctx.socket(zmq.REQ)
sock.connect('tcp://127.0.0.1:9999')

sock.send(sys.argv[1])
print(sock.recv())

sock.close()
