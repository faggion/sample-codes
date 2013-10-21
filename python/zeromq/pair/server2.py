# coding: utf-8
import zmq

if __name__ == '__main__':
    ctx = zmq.Context()

    # 自分用のコマンドポート
    cmd = ctx.socket(zmq.REP)
    cmd.bind('tcp://127.0.0.1:9999')

    # 別serverからの更新リクエストを受け付ける用のsocket
    #mst = ctx.socket(zmq.PULL)
    mst = ctx.socket(zmq.PAIR)
    mst.bind('tcp://127.0.0.1:9998')

    # 別serverへの更新リクエストを投げる用のsocket
    #slv = ctx.socket(zmq.PUSH)
    slv = ctx.socket(zmq.PAIR)
    slv.setsockopt(zmq.SNDBUF, 100000)
    slv.connect('tcp://127.0.0.1:9988')

    poll = zmq.Poller()
    poll.register(cmd, zmq.POLLIN)
    poll.register(mst, zmq.POLLIN)
    #poll.register(slv, zmq.POLLOUT)
    while True:
        sockets = dict(poll.poll(1000))
        print("poll end ...")
        # コマンドポートにコマンドリクエストが来た
        if cmd in sockets:
            if sockets[cmd] == zmq.POLLIN:
                res = cmd.recv()
                print("received message: %s" % res)

                poll.register(slv, zmq.POLLOUT)
                sout = dict(poll.poll(100))
                if slv in sout:
                    if sout[slv] == zmq.POLLOUT:
                        slv.send(res)
                        cmd.send("send ok")
                    else:
                        cmd.send("send error")
                else:
                    cmd.send("send timeout")
                poll.unregister(slv)
            else:
                print("cmd not POLLIN")

        if mst in sockets:
            if sockets[mst] == zmq.POLLIN:
                res = mst.recv()
                print("received from pair socket: %s" % (res))
            else:
                print("mst not POLLIN")
