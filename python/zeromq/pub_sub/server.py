# coding: utf-8
import zmq

if __name__ == '__main__':
    ctx = zmq.Context()

    # 自分用のコマンドポート
    cmd = ctx.socket(zmq.REP)
    cmd.bind('tcp://127.0.0.1:9999')

    # clientにリクエストを投げるためのsocket
    pub = ctx.socket(zmq.PUB)
    pub.bind('tcp://127.0.0.1:9998')

    # clientからの戻りを受け付けるsocket
    router = ctx.socket(zmq.ROUTER)
    router.bind('tcp://127.0.0.1:9997')

    poll = zmq.Poller()
    poll.register(cmd,    zmq.POLLIN)
    poll.register(router, zmq.POLLIN)
    while True:
        sockets = dict(poll.poll(1000))
        print("poll end ...")

        if cmd in sockets:
            if sockets[cmd] == zmq.POLLIN:
                print("request received from command port")
                mes = cmd.recv()
                print("received message: %s" % mes)
                #pub.send("cli1", zmq.SNDMORE)
                pub.send(mes)
                cmd.send("publish ok")
            else:
                print("cmd not POLLIN")

        if router in sockets:
            if sockets[router] == zmq.POLLIN:
                print("response received from router")
                _id = router.recv()
                res = router.recv()
                print("received from router socket(%s): %s" % (_id, res))
                router.send(_id, zmq.SNDMORE)
                router.send("ok")
            else:
                print("router error")
