# coding: utf-8
import boto, boto.ec2, re, time, os, logging
from fabric.api import run, cd, abort, require, sudo, env, parallel, task, local
from fabric.decorators import runs_once, roles, hosts
from fabric.contrib.console import confirm

SYS_NAME    = "hbase"
# http://wiki.debian.org/Cloud/AmazonEC2Image
# official debian6 image(instance disk)
IMAGE_ID    = 'ami-47693a02'

#AWS_KEYNAME = 'insecure'
#SYS_HOSTS   = [ 'client1' ]
## official debian6 image(EBS disk)
#IMAGE_ID    = 'ami-75287b30'
## official debian6 image + (sudo, rsync, sunjava)
#IMAGE_ID    = 'ami-d22c0197'
#CONN = None
#INSTANCES = []

blueprint = { "master":  ["1"],
              "clients": ["2", "3", "4"] }
#blueprint = { "master":  ["1"],
#              "clients": ["1"] }

"""

fab (ec2.conn_to_region) ec2.get_instances
fab ec2.conn_to_region ec2.start:name=NAME
fab ec2.conn_to_region ec2.start_all
fab ec2.conn_to_region ec2.terminate_all
#fab ec2.conn_to_region ec2.stop_all


"""

@task
def get_instances(user="root", region="us-west-1", group=os.getenv("USER", "develop")):
    conn = boto.ec2.connect_to_region(region)
    instances = []
    for reservation in conn.get_all_instances():
        for i in reservation.instances:
            if not group or re.match(group, i.tags.get('Name')):
                ii = {"id":i.id,
                      "public_dns": i.public_dns_name,
                      "state": i.state,
                      "name":i.tags.get("Name")}
                print("\t".join([ii['state'],
                                 ii['id'],
                                 ii['name'],
                                 ii['public_dns']]))
                instances.append(ii)
    return instances

@task
def connect(user="root", region="us-west-1", group=os.getenv("USER", "develop")):
    instances = get_instances(user, region, group)

    role = {}
    for s in range(0, len(instances)):
        if s['state'] == "running" and re.match(group, s["name"]):
            [g, sn, r, num] = s["name"].split("-", 3)
            if group == g and SYSTEM_NAME == sn:
                if not role.get(r):
                    role[r] == []
                role[r].append(s["public_dns"])
    env.roledefs.update(role)
    env.user = user

@task
def up(user="root", region="us-west-1", group=os.getenv("USER", "develop"), instance_type="m1.xlarge"):
    instances = get_instances(user, region, group)

    conn = boto.ec2.connect_to_region(region)
    for h in SYS_HOSTS:
        reservations = conn.run_instances(image_id=IMAGE_ID,
                                          instance_type=instance_type,
                                          key_name=AWS_KEYNAME)
        if not reservations or len(reservations.instances) != 1:
            abort('failed to run_instances')

        time.sleep(3)
        instance = reservations.instances[0]
        conn.create_tags([instance.id], {'Name': '%s-%s' % (SYS_NAME, h)})

@task
@roles('all')
def touch(name):
    run("touch /tmp/%s" % name)

@task
def whoami(name=os.getenv("USER")):
    print name

@task
def put_files(name, user="root", region="us-west-1"):
    pass
