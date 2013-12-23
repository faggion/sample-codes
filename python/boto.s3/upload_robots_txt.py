# coding: utf-8
import logging,boto,sys
from boto.s3.connection import S3Connection
from boto.s3.key import Key

conn = S3Connection()
bucket = conn.get_bucket(sys.argv[1])

k = Key(bucket)
k.key = 'robots.txt'
k.set_contents_from_filename('robots.txt', reduced_redundancy=True)

