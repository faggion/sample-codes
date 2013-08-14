LOOP = 50
OFF2ON = 10
ON2OFF = 10

import android
import urllib,urllib2,random,time

def make_random_num(count):
    return ''.join(map(lambda x: str(random.randint(1,9)), range(count)))

def exec_click_in(agent, cookie_id):
    params = {'agent': agent,
              'ref':'http://mikan767676.appspot.com/',
              'newinp':1,
              'uri':'http://gourmet.blogmura.com/tokyogourmet/'}
    url = 'http://link.blogmura.com/link/c/000000?' + urllib.urlencode(params)
    request = urllib2.Request(url)
    request.add_header('Host', 'link.blogmura.com')
    request.add_header('User-Agent', agent)
    request.add_header('Referer', 'http://gourmet.blogmura.com/lunch/')
    request.add_header('Cookie','click_cookie_id=%s;' % cookie_id)
    try:
        return urllib2.urlopen(request).code
    except:
        return 404

def exec_click_out(agent, cookie_id):
    url = 'http://link.blogmura.com/out/?ch=01023626&url=http%3A%2F%2Fmikan767676.appspot.com%2F'
    req = urllib2.Request(url)
    req.add_header('Host', 'link.blogmura.com')
    req.add_header('User-Agent', agent)
    req.add_header('Referer', 'http://gourmet.blogmura.com/tokyogourmet/')
    req.add_header('Cookie','click_cookie_id=%s;' % cookie_id)
    try:
        res = urllib2.urlopen(req)
        return res.code
    except urllib2.HTTPError, e:
        return e.code
    except urllib2.URLError, e:
        return 404

droid = android.Android()

for i in range(LOOP):
    agent = "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; SV1; .NET CLR 1.1.%s)" % make_random_num(4)
    cookie_id = make_random_num(16)
    # to offline
    droid.toggleAirplaneMode()
    print("offline...")
    time.sleep(OFF2ON)
    # to online
    droid.toggleAirplaneMode()
    print("online...")
    time.sleep(ON2OFF)
    print("execute click in ...")
    print(exec_click_in(agent, cookie_id))
    print("execute click out ...")
    print(exec_click_out(agent, cookie_id))



