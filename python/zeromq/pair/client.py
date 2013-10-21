# coding: utf-8

import zmq,sys

ctx = zmq.Context()
sock = ctx.socket(zmq.REQ)
sock.connect('tcp://127.0.0.1:' + sys.argv[1])

msg = ""
for i in range(1000):
    m = "%d: %s" % (i, sys.argv[2])
    sock.send(m)
    print(sock.recv())
    msg += m
    print("%d => %d" % (i, len(msg)))

sock.close()

