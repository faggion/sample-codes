# coding: utf-8

import sys,logging,traceback,time,random,re

import ConfigParser, argparse, zmq

def update_checker():
    last_checked_at = [0]

    def checker():
        now = time.time()
        if 10 < now - last_checked_at[0]:
            logging.debug("checking db update...")
            last_checked_at[0] = now

    return checker

def server_loop(conf):
    conf_server  = dict(conf.items('server'))
    conf_clients = dict(conf.items('clients'))

    ctx = zmq.Context()

    # command port (bind)
    sock_command = ctx.socket(zmq.ROUTER)
    sock_command.bind(conf_server['cmdport'])

    # socket for client response (connect)
    sock_router = ctx.socket(zmq.ROUTER)
    for cli in conf_clients['dealer_ports'].split(","):
        sock_router.connect(cli)

    # socket for publishing commmand (connect)
    sock_publisher = ctx.socket(zmq.PUB)
    for cli in conf_clients['subscriber_ports'].split(","):
        sock_publisher.connect(cli)

    checker = update_checker()
    poll = zmq.Poller()
    poll.register(sock_command, zmq.POLLIN)
    poll.register(sock_router,  zmq.POLLIN)
    while True:
        sockets = dict(poll.poll(1000))
        logging.debug("... poll end")
        if sock_command in sockets:
            if sockets[sock_command] == zmq.POLLIN:
                _id = sock_command.recv()
                logging.debug("request received from command port(%s)" % _id)
                mes = sock_command.recv()
                logging.debug("received message: %s" % mes)
                sock_publisher.send(mes)
            else:
                logging.error("cmd not POLLIN")
                break

        if sock_router in sockets:
            if sockets[sock_router] == zmq.POLLIN:
                _id = sock_router.recv()
                logging.debug("response from: " + _id)
                res = sock_router.recv()
                logging.debug("response received from router: " + res)
            else:
                logging.error("router error")
                break

        checker()

    logging.error("finished dist-server process")

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    parser = argparse.ArgumentParser(description='Ad version4 dist-server daemon')
    parser.add_argument('-c', '--conf',
                        help='config file',
                        type=file,
                        required=True)
    args = parser.parse_args()
    config = ConfigParser.SafeConfigParser()
    config.readfp(args.conf)
    server_loop(config)

