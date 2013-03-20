# coding: utf-8
import boto, boto.ec2, re, time, os, logging
from fabric.api import run, cd, abort, require, sudo, env, parallel, task, local
from fabric.decorators import runs_once, roles, hosts
from fabric.contrib.console import confirm

SYS_NAME    = "hbase"
# http://wiki.debian.org/Cloud/AmazonEC2Image
# official debian6 image(instance disk)
IMAGE_ID    = 'ami-47693a02'
SEPARATOR   = "-"
KEYNAME     = 'insecure'
BLUEPRINT   = { "master":  ["1"],
                "clients": ["2", "3", "1"] }

def update_status(group):
    status = {}
    for b in BLUEPRINT:
        for n in range(0, len(BLUEPRINT[b])):
            name = SEPARATOR.join([group, SYS_NAME, BLUEPRINT[b][n]])
            status[name] = None
    return status

def update_role_and_status(conn, group):
    role = {}
    status = update_status(group)
    all  = {}
    for reservation in conn.get_all_instances():
        for i in reservation.instances:
            name = i.tags.get("Name", "")
            host = name.split("-")
            if len(host) != 3 or \
               host[0] != group or \
               host[1] != SYS_NAME or \
               i.state == "terminated":
                continue
            status[name] = {
                "id": i.id,
                "public_dns": i.public_dns_name,
                "state": i.state,
                "roles": []
                }
            for b in BLUEPRINT:
                if host[2] in BLUEPRINT[b]:
                    status[name]["roles"].append(b)
                    if i.state != "running":
                        continue
                    if not role.get(b):
                        role[b] = []
                    role[b].append(i.public_dns_name)
                    all[i.public_dns_name] = 1
    role["ALL"] = all.keys()
    return [role, status]

@task
def connect(region="us-west-1", user="root", group=os.getenv("USER", "develop")):
    env.conn   = boto.ec2.connect_to_region(region)
    [role, status] = update_role_and_status(env.conn, group)
    env.roledefs.update(role)
    env.user   = user
    env.status = status
    
@task
def get_instances(region="us-west-1", user="root", group=os.getenv("USER", "develop")):
    role   = env.roledefs
    status = env.status

    print "Instances:"
    for name in status:
        if status[name] == None:
            print "%s: Not Created" % name
        else:
            print "%s: state=%s, id=%s, public_dns=%s" % (name,
                                                          status[name]['state'],
                                                          status[name]['id'],
                                                          status[name]['public_dns'])

    print ""
    print "Roles:"
    for r in role:
        print "  %s" % r
        for s in range(0,  len(role[r])):
            print "    %s" % role[r][s]

@task
def start_all():
    conn   = env.conn
    role   = env.roledefs
    status = env.status

    for s in status:
        if status[s] != None:
            abort('failed to start all instances because instances are already created')

    reservations = conn.run_instances(image_id=IMAGE_ID,
                                      key_name=KEYNAME,
                                      instance_type=instance_type,
                                      min_count=len(status),
                                      max_count=len(status))

    if not reservations or len(reservations.instances) != len(status):
        abort('failed to run_instances')

    print "sent start request, please wait ..."
    time.sleep(2)

    for s in status:
        instance = reservations.instances.pop()
        conn.create_tags([instance.id], {'Name': s})

@task
def terminate_all(region="us-west-1", user="root", group=os.getenv("USER", "DEV"), instance_type="m1.small"):
    conn   = env.conn
    role   = env.roledefs
    status = env.status

    for s in status:
        if status[s] != None and status[s].get('state') != 'running':
            abort('failed to start all instances because instances are not running')

    ids = []
    for name in status:
        if status[name].get('state') == "running":
            ids.append(status[name]["id"])
    conn.terminate_instances(ids)

# ---------------

@task
def get_all_instances(region="us-west-1"):
    conn = boto.ec2.connect_to_region(region)
    print "All instances:"
    for reservation in conn.get_all_instances():
        for i in reservation.instances:
            print "%s: state=%s, name=%s" % (i.id, i.state, i.tags.get('Name'))

@task
@roles('ALL')
@parallel
def touch(name):
    run("touch /tmp/%s" % name)

# ---------------

"""

role = {
    "master": [ "ec2-XX-XX-XX-XX.amazon.com" ]
    "clients": [ "ec2-XX-XX-XX-XX.amazon.com",
                 "ec2-XX-XX-XX-XX.amazon.com",
                 "ec2-XX-XX-XX-XX.amazon.com"]
}
status = {
    "USER-NAME-1": { "roles":["master", "clients"], public_dns:"ec2-XX-XX-XX-XX.amazon.com", "status":"running", "id":"i12345678" },
    "USER-NAME-2": { "roles":["clients"], public_dns:"ec2-XX-XX-XX-XY.amazon.com", "status":"running", "id":"i12345679" },
    "USER-NAME-3": { "roles":["clients"], public_dns:"ec2-XX-XX-XX-XZ.amazon.com", "status":"running", "id":"i12345670" },
    "USER-NAME-4": { "roles":["clients"], public_dns:"ec2-XX-XX-XX-XW.amazon.com", "status":"running", "id":"i12345671" },
}

"""
