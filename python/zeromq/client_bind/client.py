# coding: utf-8

import zmq,sys

if __name__ == "__main__":
    ctx = zmq.Context()
    sub = ctx.socket(zmq.SUB)
    sub.setsockopt(zmq.SUBSCRIBE, '')
    sub.bind(sys.argv[1])

    #push = ctx.socket(zmq.PUSH)
    push = ctx.socket(zmq.DEALER)
    push.setsockopt(zmq.IDENTITY, sys.argv[3])
    push.bind(sys.argv[2])

    while True:
        print("receiving ...")
        mes = sub.recv()
        print("received from sub socket: %s" % (mes))
        push.send("return message: %s" % (mes * 2))
