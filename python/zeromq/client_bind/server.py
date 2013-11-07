# coding: utf-8
import zmq,sys

if __name__ == '__main__':
    ctx = zmq.Context()

    # 自分用のコマンドポート
    cmd = ctx.socket(zmq.REP)
    cmd.bind(sys.argv[1])

    # clientにリクエストを投げるためのsocket(server -> client でconnect)
    pub = ctx.socket(zmq.PUB)
    pub.connect('tcp://127.0.0.1:9990')
    pub.connect('tcp://127.0.0.1:9991')

    # clientからの戻りを受け付けるsocket(server -> client でconnect)
    #pull = ctx.socket(zmq.PULL)
    pull = ctx.socket(zmq.ROUTER)
    pull.connect('tcp://127.0.0.1:9980')
    pull.connect('tcp://127.0.0.1:9981')

    poll = zmq.Poller()
    poll.register(cmd,  zmq.POLLIN)
    poll.register(pull, zmq.POLLIN)
    while True:
        sockets = dict(poll.poll(1000))
        print("poll end ...")

        if cmd in sockets:
            if sockets[cmd] == zmq.POLLIN:
                print("request received from command port")
                mes = cmd.recv()
                print("received message: %s" % mes)
                pub.send(mes)
                cmd.send("publish ok")
            else:
                print("cmd not POLLIN")

        if pull in sockets:
            if sockets[pull] == zmq.POLLIN:
                _id = pull.recv()
                print("response from: " + _id)
                res = pull.recv()
                print("response received from pull: " + res)
            else:
                print("router error")

