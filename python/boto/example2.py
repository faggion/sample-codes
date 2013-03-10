import boto, os, sys, logging
import boto.ec2

def get_all_ins(c):
    reservations = c.get_all_instances()
    for r in reservations:
        for i in r.instances:
            print i.image_id
            #print i.ramdisk
            print i.tags.get('Name')
            #print i.kernel
            #print i.image_id
            #print i.platform
            #print i.instance_type
            #print i.instance_profile
            print '-----'

if __name__ == '__main__':
    region_name = 'us-west-1'
    regions = boto.ec2.regions()
    print regions
    for r in regions:
        if r.name == region_name:
            break
    conn = boto.connect_ec2(region=r)
    get_all_ins(conn)
    #print conn.get_all_instances()
    #print conn.get_all_security_groups()

