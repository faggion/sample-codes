# coding: utf-8
import sys
sys.path.insert(0, '..')
sys.path.insert(0, '../lib.zip')

import logging, os, traceback, json
import requests, argparse, csv

def request_api(path, method, data=None, headers={}):
    headers['Content-type'] = 'application/json; charset=utf-8'
    d = None
    if data:
        d = json.dumps(data)
    return getattr(requests, method)('http://localhost:8080/api/v1'+path,data=d,headers=headers)

def truncate_data(kind):
    r = request_api('/%s' % kind, 'get')
    tag_ids = json.loads(r.text)

    for i, t in enumerate(tag_ids):
        r = request_api('/%s/%d' % (kind, t), 'delete')

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    parser = argparse.ArgumentParser(description='')

    parser.add_argument('-k', '--kind', type=str, required=True, help="kind")
    args = parser.parse_args()
    truncate_data(args.kind)
