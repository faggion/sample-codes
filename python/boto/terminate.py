import boto, sys
import boto.ec2

def get_all_ins(c):
    reservations = c.get_all_instances()
    for r in reservations:
        for i in r.instances:
            print i.id
            print i.tags.get('Name')
            #print i.kernel
            print i.image_id
            #print i.platform
            #print i.instance_type
            #print i.instance_profile
            print '-----'

region_name = 'us-west-1'
for r in boto.ec2.regions():
    if r.name == region_name:
        break
conn = boto.connect_ec2(region=r)

print conn.terminate_instances(instance_ids=sys.argv[1:])
