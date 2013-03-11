from fabric.api import task, run, env, parallel
from fabric.decorators import roles, hosts

@task
def create():
    pass

@task
def delete():
    pass

@task
def passwd():
    pass

@task
def disable_permit_root_login():
    pass

@task
def enable_permit_root_login():
    pass

@task
@parallel
def do_something():
    run("touch /tmp/fabric_modules")

