# coding: utf-8
# message_str = '{"success":[], "warning":[], "danger":[]}'
import logging, json
from google.appengine.api import users, memcache

CACHE_EXP = 60
CACHE_NAME_SPACE = 'M'

def cachekey(userid):
    return "%s:%s" % (CACHE_NAME_SPACE, userid)

def set(userid, key, body):
    message = {"success":[], "warning":[], "danger":[]}
    saved_message = get(userid, clear=False)
    if saved_message:
        message = saved_message

    message[key].append(body)
    return memcache.set(cachekey(userid), json.dumps(message), CACHE_EXP)

def get(userid, clear=True):
    val = memcache.get(cachekey(userid))
    if not val:
        return None
    if clear:
        memcache.delete(cachekey(userid))
    return json.loads(val)

