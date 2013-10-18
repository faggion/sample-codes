# coding: utf-8

import zmq

if __name__ == '__main__':
    ctx = zmq.Context()
    io  = ctx.socket(zmq.ROUTER)
    io.bind('tcp://*:5555')
    cmd = ctx.socket(zmq.REP)
    #cmd.bind('inproc://tmp/cmdport')
    cmd.bind('tcp://*:9999')

    poll = zmq.Poller()
    poll.register(io, zmq.POLLIN)
    poll.register(cmd, zmq.POLLIN)
    while True:
        sockets = dict(poll.poll(1000))
        print("poll end ...")
        if io in sockets:
            if sockets[io] == zmq.POLLIN:
                _id = io.recv()
                res = io.recv()
                print("id: %s, received: %s" % (_id, res))
                io.send(_id, zmq.SNDMORE)
                io.send(res)
        if cmd in sockets:
            if sockets[cmd] == zmq.POLLIN:
                res = cmd.recv()
                print("received from cmd: %s" % (res))
                cmd.send(res)



