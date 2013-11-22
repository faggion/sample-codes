# coding: utf-8
import requests,sys

#r = requests.get('http://localhost:5000/adv4/dist/api/1.0/deliver/' + sys.argv[1])
#print(r.text)

#r = requests.post('http://localhost:5000/adv4/dist/api/1.0/deliver/create')
r = requests.delete('http://localhost:5000/adv4/dist/api/1.0/deliver/3')
print(r.text)
