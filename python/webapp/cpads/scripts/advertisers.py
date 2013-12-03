# coding: utf-8

import logging, requests, sys, os, traceback, json

url_adv = 'http://localhost:8080/a/adv'

def main():
    advs = [
        {"name": "luxa",
         "id": 1,
         "media_id": 1,
         "expire": 14,
         "active": True,
         "average": 7000,
         "ratio": 3.0,
         "score": 210.0,
         "vc_pid": "880694021"},
        {"name": "kumapon",
         "id": 2,
         "media_id": 1,
         "expire": 10,
         "active": True,
         "average": 6000,
         "ratio": 4.0,
         "score": 240.0,
         "vc_pid": "882358919"}
        ]
    for adv in advs:
        ret = requests.put(url_adv,
                           data=json.dumps(adv),
                           headers={"content-type": "application/json"})
        logging.debug(ret.text)

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    main()
