# coding: utf-8
import zmq

if __name__ == '__main__':
  ctx = zmq.Context()

  # 自分用のコマンドポート
  cmd = ctx.socket(zmq.REP)
  cmd.bind('tcp://127.0.0.1:9989')

  # 別serverからの更新リクエストを受け付ける用のsocket
  #mst = ctx.socket(zmq.PULL)
  mst = ctx.socket(zmq.PAIR)
  mst.setsockopt(zmq.RCVBUF, 100000)
  mst.bind('tcp://127.0.0.1:9988')

  # 別serverへの更新リクエストを投げる用のsocket
  #slv = ctx.socket(zmq.PUSH)
  slv = ctx.socket(zmq.PAIR)
  slv.connect('tcp://127.0.0.1:9998')

  poll = zmq.Poller()
  poll.register(cmd, zmq.POLLIN)
  poll.register(mst, zmq.POLLIN)
  while True:
    sockets = dict(poll.poll(1000))
    print("poll end ...")
    # コマンドポートにコマンドリクエストが来た
    if cmd in sockets:
      if sockets[cmd] == zmq.POLLIN:
        res = cmd.recv()
        print("received message: %s" % res)
        slv.send(res)
        cmd.send("send ok")

        #if res == "slave_conn":
        #  slv.connect('tcp://127.0.0.1:9998')
        #  cmd.send("slv connect ok")
        #elif res == "slave_close":
        #  slv.close()
        #  cmd.send("slv close ok")
        #else:
        #  print("received message: %s" % res)
        #  slv.send(res)
        #  cmd.send("send ok")
      else:
        print("cmd not POLLIN")

    if mst in sockets:
      if sockets[mst] == zmq.POLLIN:
        res = mst.recv()
        print("received from pair socket: %s" % (res))
      else:
        print("mst not POLLIN")



