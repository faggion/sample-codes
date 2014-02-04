# coding: utf-8
import sys
sys.path.insert(0, '..')
sys.path.insert(0, '../lib.zip')

import logging, os, traceback, json, time
import requests, argparse, csv

BASEURL = 'http://localhost:8080/api/v1'

def request_api(path, method, data=None, headers={}):
    headers['Content-type'] = 'application/json; charset=utf-8'
    d = None
    if data:
        d = json.dumps(data)
    return getattr(requests, method)(BASEURL+path,data=d,headers=headers)

def insert_tags(fp):
    row = csv.reader(fp, delimiter='\t')
    header = next(row)
    for r in row:
        if 0 < len(r) and r[0] and r[0].startswith('#'):
            continue
        data = dict(zip(header, r))
        t = {'num': int(data['num']),
             'name': data['name'],
             'value': data['value'],
             'is_end': bool(data['is_end'])}
        if data['parent']:
            t['parent'] = int(data['parent'])
        r = request_api('/tag', 'put', t)
        logging.debug(r.status_code)
        time.sleep(0.15)

def insert_contents(fp):
    row = csv.reader(fp, delimiter='\t')
    header = next(row)
    for r in row:
        data = dict(zip(header, r))
        c = {"title": data['title'],
             "body": data['body'],
             "posted_at": data['posted_at'],
             "tag_nums": [int(n) for n in data['tag_nums'].split(",")]}

        if data['num']:
            c['num'] = int(data['num'])

        r = request_api('/content', 'put', data=c)
        logging.debug(r.status_code)

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-m', '--mode', type=str, required=True, help="mode")
    parser.add_argument('-f', '--file', type=argparse.FileType('r'), required=True, help="file")
    #parser.add_argument('-t', '--truncate', type=bool, required=False, help="date truncate")
    args = parser.parse_args()

    if args.mode == 'insert_tags':
        #insert_tags(args.file, args.truncate)
        insert_tags(args.file)

    if args.mode == 'insert_contents':
        insert_contents(args.file)
