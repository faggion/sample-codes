# coding: utf-8

import appengine_config

import logging, os, sys, traceback, json
import requests, argparse, csv

def request_api(path, method, data=None, headers={}):
    headers['Content-type'] = 'application/json; charset=utf-8'
    d = None
    if data:
        d = json.dumps(data)
    return getattr(requests, method)('http://localhost:8080/api/v1'+path,data=d,headers=headers)

def insert_tags(fp, truncate=False):
    r = request_api('/tag', 'get')

    row = csv.reader(fp, delimiter='\t')
    header = next(row)
    for r in row:
        data = dict(zip(header, r))
        if args.mode == 'insert_tag':
            insert_tag(data)
        elif args.mode == 'insert_content':
            pass

    r = request_api('/tag', 'put', data)
    logging.debug(r.status_code)

def insert_content(data):
    pass

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-m', '--mode', type=str, required=True, help="mode")
    parser.add_argument('-f', '--file', type=argparse.FileType('r'), required=True, help="file")
    parser.add_argument('-t', '--truncate', type=bool, required=False, help="date truncate")
    args = parser.parse_args()

    if args.mode == 'insert_tag':
        insert_tag(args.file, args.truncate)
