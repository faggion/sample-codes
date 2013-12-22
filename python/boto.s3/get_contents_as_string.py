# coding: utf-8
import logging,boto
from boto.s3.connection import S3Connection
from boto.s3.key import Key

logging.error('connecting ...')
conn = S3Connection()
logging.error('connected.')
logging.error('getting bucket ...')
bucket = conn.get_bucket('t.tnky.pw')
logging.error('got bucket: %s' % bucket.name)

k = Key(bucket)
k.key = 'test.html'
logging.error('got contents')
print(k.get_contents_as_string())
