import requests
import logging

r = requests.get('http://localhost:10080/')
logging.error(r.content)

r = requests.post('http://localhost:10080/')
logging.error(r.content)

r = requests.put('http://localhost:10080/')
logging.error(r.content)

r = requests.delete('http://localhost:10080/')
logging.error(r.content)
