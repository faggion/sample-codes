# coding: utf-8

import zmq,sys

ctx = zmq.Context()
sock = ctx.socket(zmq.REQ)
sock.connect(sys.argv[1])

for i in range(int(sys.argv[3])):
    sock.send(sys.argv[2] * (i+1))
    print(sock.recv())

sock.close()
