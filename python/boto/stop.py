import boto, sys
import boto.ec2

region_name = 'us-west-1'
conn = boto.ec2.connect_to_region(region_name)
print conn.stop_instances(instance_ids=sys.argv[1:])
