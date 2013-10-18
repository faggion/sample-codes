# coding: utf-8

import zmq

ctx = zmq.Context()
sock = ctx.socket(zmq.REQ)
#sock.connect('inproc://tmp/cmdport')
sock.connect('tcp://127.0.0.1:9999')
sock.send('from cmd port')
print sock.recv()

