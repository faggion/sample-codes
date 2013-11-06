# coding: utf-8

import zmq, sys

ctx = zmq.Context()
sock = ctx.socket(zmq.DEALER)
sock.setsockopt(zmq.IDENTITY, 'id1')
#sock.connect('tcp://127.0.0.1:5555')
for a in sys.argv[2:]:
    sock.connect(a)

for i in range(int(sys.argv[1])):
    sock.send('hello')
print sock.recv()

