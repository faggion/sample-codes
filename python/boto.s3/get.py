# coding: utf-8
import logging,boto
from boto.s3.connection import S3Connection
from boto.s3.key import Key

#logging.getLogger().setLevel(logging.DEBUG)
logging.error('connecting ...')
conn = S3Connection()
logging.error('connected.')
logging.error('getting all buckets ...')
for b in conn.get_all_buckets():
    logging.error('got bucket: %s' % b.name)
    for key in b.list(prefix='test'):
        print key
