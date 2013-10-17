# -*- coding: utf-8 -*-
# http://ymotongpoo.hatenablog.com/entry/20111217/1324125102

import time
from datetime import datetime
import os,sys,lockfile
import daemon

def daemon_process():
    while True:
        print( "pid: %d, ppid: %d, time: %s" %
               (os.getpid(), os.getppid(), datetime.now()) )
        sys.stdout.flush()
        time.sleep(5)

working_dir = os.path.abspath(os.path.dirname(__file__))

context = daemon.DaemonContext(
    working_directory = working_dir,
    stdout = open("stdout_file.txt", "w+"),
    stderr = open("stderr_file.txt", "w+")
)

if __name__ == '__main__':
    with context:
        daemon_process()
