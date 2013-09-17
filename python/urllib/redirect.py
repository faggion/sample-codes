# coding: utf-8
import urllib2

class FollowRedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_302(self, req, fp, code, msg, headers):
        return urllib2.HTTPRedirectHandler.http_error_302(self, req, fp, code, msg, headers)
    http_error_301 = http_error_303 = http_error_307 = http_error_302

opener   = urllib2.build_opener(FollowRedirectHandler, urllib2.HTTPCookieProcessor())
urllib2.install_opener(opener)

request  = urllib2.Request("http://localhost:10080/rd")
request.add_header('Cookie', 'username=test')
response = urllib2.urlopen(request)
