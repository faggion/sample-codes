# coding: utf-8

import zmq,sys

if __name__ == "__main__":
    ctx = zmq.Context()
    sub = ctx.socket(zmq.SUB)
    sub.setsockopt(zmq.SUBSCRIBE, '')
    sub.connect('tcp://127.0.0.1:9998')

    dealer = ctx.socket(zmq.DEALER)
    dealer.setsockopt(zmq.IDENTITY, sys.argv[1])
    dealer.connect('tcp://127.0.0.1:9997')

    while True:
        print("receiving ...")
        mes = sub.recv()
        print("received from sub socket: %s" % (mes))
        #print("(%s) received from sub socket: %s" % (_id, mes))

        dealer.send("return message: %s" % (mes * 2))
        print(dealer.recv())
