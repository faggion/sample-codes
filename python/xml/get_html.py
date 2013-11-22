# coding: utf-8
import requests

url = 'http://luxa.jp/'
headers = {
    "Set-Cookie": "LXTOPCTGR=1-0-0-0-0-0-0-0-1-0-0-0-0-0-0; LXAREA=tokyo",
}
r = requests.get(url, headers=headers)

print(r.text.encode('utf-8'))
