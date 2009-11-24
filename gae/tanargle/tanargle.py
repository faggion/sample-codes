# -*- coding: utf-8 -*-
from google.appengine.api import users
from django.utils import simplejson

print 'Content-Type: application/json'
print ''

back = "/"
res  = {}
user = users.get_current_user()
if not user:
    res["nickname"] = 'ゲストさん'
    res["login"]    = users.create_login_url(back)
else:
    res["nickname"] = user.nickname()
    res["user_id"]  = user.user_id()
    res["logout"]   = users.create_logout_url(back)


print simplejson.dumps(res, ensure_ascii=False)





