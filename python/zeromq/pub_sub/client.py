# coding: utf-8

import zmq

if __name__ == "__main__":
    ctx = zmq.Context()
    sub = ctx.socket(zmq.SUB)
    sub.setsockopt(zmq.SUBSCRIBE, '')
    #sub.setsockopt(zmq.SUBSCRIBE, 'cli1')
    sub.connect('tcp://127.0.0.1:9998')

    dealer = ctx.socket(zmq.DEALER)
    dealer.setsockopt(zmq.IDENTITY, 'cli1')
    dealer.connect('tcp://127.0.0.1:9997')

    while True:
        print("receiving ...")
        #_id = sub.recv()
        mes = sub.recv()
        print("received from sub socket: %s" % (mes))
        #print("(%s) received from sub socket: %s" % (_id, mes))

        dealer.send("return message: %s" % (mes * 2))
        print(dealer.recv())
