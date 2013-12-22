# coding: utf-8
import logging,boto
from boto.s3.connection import S3Connection
from boto.s3.key import Key

conn = S3Connection()
bucket = conn.get_bucket('t.tnky.pw')

k = Key(bucket)
k.key = 'test2.html'
k.set_contents_from_filename('test.html')
k.get_contents_to_filename('/tmp/test.html')
