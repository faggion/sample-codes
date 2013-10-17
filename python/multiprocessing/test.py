#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import multiprocessing
import daemon

class NeetsDaemon(object):
    def __init__(self, processes):
        self.processes = processes
    def start(self):
        for i in range(self.processes):
            # 新しいプロセスを作る
            p = multiprocessing.Process(target=self._main_loop)
            # デーモンフラグを有効にすると親プロセスが死んだとき一緒に死ぬようになる
            p.daemon = True
            # プロセスを開始する
            p.start()
        # 自分もメインループに入る
        self._main_loop()

    def _main_loop(self):
        while True:
            time.sleep(1)

if __name__ == '__main__':
    with daemon.DaemonContext():
        # 子プロセスは 3 つ
        neetsd = NeetsDaemon(3)
        # デーモンを開始する
        neetsd.start()
