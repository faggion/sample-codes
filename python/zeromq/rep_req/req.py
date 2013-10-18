# coding: utf-8

import zmq

ctx = zmq.Context()
sock = ctx.socket(zmq.REQ)
sock.connect('tcp://127.0.0.1:5555')

sock.send('hello')
print sock.recv()

