# coding: utf-8

from fabric.api import run, cd, abort, require, sudo, env, parallel
from fabric.decorators import runs_once, roles, hosts
from fabric.contrib.console import confirm

def hello():
    print('Hello, Tanarky.')

def production():
    env.roledefs.update({
            'webservers': ['localhost'],
            'dbservers': ['localhost:22', 'localhost'],
            })

def staging():
    env.roledefs.update({
            'webservers': ['127.0.0.1'],
            'dbservers': ['satoshi@127.0.0.1:22', 'localhost'],
            })

@parallel
@roles('dbservers')
def do_release():
    run("touch /tmp/released_to_webservers")

@parallel
@roles('dbservers')
def do_ls_var():
    run("ls /var")

@hosts('localhost')
def do_something():
    run("touch /tmp/fabric")
    sudo("touch /tmp/fabric_root")

