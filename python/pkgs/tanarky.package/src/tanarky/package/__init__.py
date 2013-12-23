# coding: utf-8
import logging, sys, os, traceback
import argparse, boto, re
from boto.s3.connection import S3Connection
from boto.s3.key import Key

"""

- /robots.txt
- /source/***.tgz: tgz置き場
- /simple/...: html置き場

"""

FILENAME_PATTERN = re.compile(r'(([^/]*?)-([0-9\.]+).tar.gz)')
ROOT_PATH   = '/'
SOURCE_PATH = 'source/'
HTML_PATH   = 'simple/'
INDEX_FILE  = 'index.html'

class Uploader(object):
    @classmethod
    def update_html(cls, bucket):
        all_packages = {}
        for key in bucket.list(prefix=SOURCE_PATH):
            match = re.search(FILENAME_PATTERN, key.name)
            if not match:
                continue
            package_file = match.group(1)
            package_name = match.group(2)
            package_ver  = match.group(3)
            if not package_name in all_packages:
                all_packages[package_name] = []
            all_packages[package_name].append(package_file)

        logging.debug(all_packages)

        # all package index
        root_index_html = ['<!DOCTYPE html>',
                           '<html><head><meta charget="utf-8"><title>Simple index</title></head><body>',
                           '<ul>']

        for p in all_packages.keys():
            root_index_html.append('<li><a href="%s%s%s/%s">%s</a></li>' % (ROOT_PATH, HTML_PATH, p, INDEX_FILE, p))

            # package index
            package_index_html = ['<!DOCTYPE html>',
                                  '<html><head><meta charget="utf-8"><title>%s</title></head><body>' % p,
                                  '<h1>%s</h1><ul>' % p]
            for v in all_packages[p]:
                package_index_html.append('<li><a href="%s%s%s">%s</a></li>' % (ROOT_PATH, SOURCE_PATH, v, v))
            package_index_html.append('</ul></body></html>')
            k = Key(bucket)
            k.key = ROOT_PATH + HTML_PATH + p + "/" + INDEX_FILE
            k.set_contents_from_string("\n".join(package_index_html),
                                       headers={'Content-type':'text/html; charset=utf-8'})

        root_index_html.append('</ul></body></html>')

        k = Key(bucket)
        k.key = ROOT_PATH + HTML_PATH + INDEX_FILE
        k.set_contents_from_string("\n".join(root_index_html),
                                   headers={'Content-type':'text/html; charset=utf-8'})

    @classmethod
    def upload_tgz(cls, bucket):
        logging.debug(cls.args.file.name)
        filename = os.path.basename(cls.args.file.name)
        logging.debug(filename)
        match = re.search(FILENAME_PATTERN, filename)
        if not match:
            raise NameError, 'Package file name is invalid: ' + filename
        logging.debug(match.group(2))
        logging.debug(match.group(3))

        k = Key(bucket)
        k.key = SOURCE_PATH + filename
        k.set_contents_from_filename(cls.args.file.name)

    @classmethod
    def cli(cls):
        cls.parser = argparse.ArgumentParser(description='tanarky package uploader')
        cls.parser.add_argument('--file',
                                metavar='F',
                                type=file,
                                required=True,
                                help='package tar.gz file')

        cls.parser.add_argument('--bucket',
                                metavar='B',
                                type=str,
                                required=True,
                                help='S3 bucket name')

        cls.args = cls.parser.parse_args()

        conn = S3Connection()
        bucket = conn.get_bucket(cls.args.bucket)
        cls.upload_tgz(bucket)
        cls.update_html(bucket)

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    Uploader.cli()
