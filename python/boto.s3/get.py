# coding: utf-8
import logging,boto
from boto.s3.connection import S3Connection
from boto.s3.key import Key

conn = S3Connection('foo', 'bar')
print conn.get_all_buckets()

"""

#mybucket = conn.get_bucket('eventregist.com.ticket-img')
#print mybucket.list()

#b = conn.get_bucket('eventregist.com.ticket-img')
#k = Key(b)
#k.key = 'T20130908032001a3e5838e64de028c1e7b94779cbc5f21d4edb617.png'
#print k.get_contents_as_string()

b = conn.get_bucket('eventregist.com.ticket-img.stg')
for k in b.get_all_keys():
    print k.name

"""
