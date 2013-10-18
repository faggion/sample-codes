# coding: utf-8

import zmq

if __name__ == '__main__':
    ctx = zmq.Context()
    io  = ctx.socket(zmq.ROUTER)
    io.bind('tcp://*:5555')

    poll = zmq.Poller()
    poll.register(io, zmq.POLLIN)
    while True:
        sockets = dict(poll.poll(1000))
        print("poll end ...")
        for sock in sockets:
            _id = sock.recv()
            res = sock.recv()
            print("id: %s, received: %s" % (_id, res))
            sock.send(_id, zmq.SNDMORE)
            sock.send(res)



