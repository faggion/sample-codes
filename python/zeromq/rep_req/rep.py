# coding: utf-8

import zmq
from zmq.eventloop import ioloop

loop = ioloop.IOLoop.instance()

ctx = zmq.Context()
sock = ctx.socket(zmq.REP)
sock.bind('tcp://127.0.0.1:5555')

def rep_handler(sock, events):
  msg = sock.recv()
  sock.send(msg)

loop.add_handler(sock, rep_handler, zmq.POLLIN)

loop.start()
