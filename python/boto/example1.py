import boto, boto.ec2, sys, time
from boto.ec2.blockdevicemapping import BlockDeviceType
from boto.ec2.blockdevicemapping import BlockDeviceMapping

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

#print conn.run_instances(image_id='ami-75287b30')
#print conn.run_instances(image_id='ami-71287b34')

mapping = BlockDeviceMapping()
eph0 = BlockDeviceType()
eph1 = BlockDeviceType()
eph0.ephemeral_name = 'ephemeral0'
eph1.ephemeral_name = 'ephemeral1'
mapping['/dev/xvdc'] = eph0
mapping['/dev/xvdd'] = eph1

print conn.run_instances(image_id='ami-75287b30',
                         instance_type='m1.medium',
                         key_name='debian6',
                         block_device_map=mapping)

#print conn.terminate_instances(instance_ids=['i-8bd812d3'])
#print sys.argv[1:]

#for i in conn.get_all_images(filters={ "architecture":"x86_64", "state":"available", 'image-id':'ami-75287b30' }):
#for i in conn.get_all_images(filters={ "architecture":"x86_64", "state":"available", "description":"*Debian*" }):
#for i in conn.get_all_images(filters={ "architecture":"x86_64", "state":"available", "description":"*Ubuntu*" }):
#for i in conn.get_all_images(filters={ "architecture":"x86_64", "owner_alias":"amazon" }):
#    print i.location
    #print i.kernel_id
    #print i.name

#get_all_ins(conn)

#for i in reservations.instances:
#    print i
