# coding: utf-8

import zmq

ctx = zmq.Context()
sock = ctx.socket(zmq.REQ)
sock.connect('tcp://127.0.0.1:5555')

# REQ側はレスポンスを受け取るまで新たなリクエストを出来ないし
# REP側はレスポンスを返すまで他のリクエストを受け取れない
sock.send('hello')
#sock.send('hello')
print sock.recv()

