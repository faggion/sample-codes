# coding: utf-8
import logging,boto, sys
from boto.s3.connection import S3Connection
from boto.s3.key import Key

#logging.getLogger().setLevel(logging.DEBUG)
logging.error('connecting ...')
conn = S3Connection()
logging.error('connected.')
logging.error('getting all buckets ...')
b = conn.get_bucket(sys.argv[1])
logging.error('got bucket: %s' % b.name)
for key in b.list(prefix=sys.argv[2]):
    key.delete()
