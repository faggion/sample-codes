# coding: utf-8
import logging,boto
from boto.s3.connection import S3Connection
from boto.s3.key import Key

conn = S3Connection()
bucket = conn.get_bucket('t.tnky.pw')

k = Key(bucket)
k.key = 'test.html'
body = '<html><body><h1>test.html from set_contents_from_string</h1><body></html>'
k.set_contents_from_string(body, headers={'Content-type':'text/html; charset=utf-8'})
