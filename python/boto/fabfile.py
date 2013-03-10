# coding: utf-8
from fabric.api import local, abort
import logging, time, boto, boto.ec2
import boto.ec2.blockdevicemapping

def get_regions():
    for r in boto.ec2.regions():
        print r.name

def get_instances(region="us-west-1"):
    print "region = %s" % (region)
    conn = boto.ec2.connect_to_region(region)
    print "-----"
    for reservation in conn.get_all_instances():
        for i in reservation.instances:
            print "%s: id=%s, type=%s, name=%s" % (i.state, i.id, i.instance_type, i.tags.get('Name'))
    print "-----"

def create_instance_debian6(region="us-west-1", type="m1.medium"):
    print "region = %s" % (region)
    conn = boto.ec2.connect_to_region(region)
    if not conn:
        abort('failed to connect to %s' % region)

    # http://wiki.debian.org/Cloud/AmazonEC2Image
    # official debian6 image(instance disk)
    image_id = 'ami-47693a02'
    reservations = conn.run_instances(image_id=image_id,
                                      instance_type='m1.medium',
                                      key_name='satoshi-tanaka')

    ## official debian6 image(instance-store disk)
    #image_id = 'ami-71287b34'
    #reservations = conn.run_instances(image_id=image_id,
    #                                  instance_type='m1.medium',
    #                                  key_name='debian6')

    ## official debian6 image(instance-store disk)
    #image_id = 'ami-71287b34'
    #reservations = conn.run_instances(image_id=image_id,
    #                                  instance_type='m1.medium',
    #                                  key_name='debian6')

    if not reservations or len(reservations.instances) != 1:
        abort('failed to run_instances')

    instance = reservations.instances[0]
    conn.create_tags([instance.id], {'Name': 'testfab1'})

    print('Waiting for instance to start...')

    for i in range(0,10):
        time.sleep(10)
        status = instance.update()
        if status == 'running':
            print('New instance "' + instance.id + '" accessible at ' + instance.public_dns_name)
            break
        else:
            print('Instance status: ' + status)

