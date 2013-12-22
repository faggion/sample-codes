# coding: utf-8
import logging,boto
from boto.s3.connection import S3Connection
from boto.s3.key import Key

conn = S3Connection()
bucket = conn.get_bucket('t.tnky.pw')

k = Key(bucket)
k.key = '/testdir/test.txt'
body = 'this is test text'
k.set_contents_from_string(body, headers={'Content-type':'text/plain; charset=utf-8'})
