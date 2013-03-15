# coding: utf-8

from fabric.api import run, cd, abort, require, sudo, env, parallel, task, put
from fabric.decorators import runs_once, roles, hosts
from fabric.contrib.console import confirm

#env.hosts = ['localhost']

@task
def put_file():
    put('foo.txt', '/tmp/')

@task
def put_dir():
    put('bar', '/tmp/')
