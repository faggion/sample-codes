# coding: utf-8

import logging, sys, os, argparse, csv
import models
from sqlalchemy.orm import sessionmaker, relationship

def insert_data(session, data, m):
    if not data:
        return

    t = m()
    for k, v in data.iteritems():
        if v:
            setattr(t, k, v)
        else:
            setattr(t, k, None)
    session.merge(t, load=True)

def main():
    parser = argparse.ArgumentParser(description='insert initial data')

    parser.add_argument('--tag_keys', '-k', type=argparse.FileType('r'), help="tag_keys tsv files")
    parser.add_argument('--tag_sets', '-s', type=argparse.FileType('r'), help="tag_sets tsv files")
    parser.add_argument('--articles', '-a', type=argparse.FileType('r'), help="articles tsv files")
    parser.add_argument('--tagging',  '-t', type=argparse.FileType('r'), help="tagging tsv files")
    parser.add_argument('--version',  '-v', action="version", version="%(prog)s 1.0")

    args = parser.parse_args()

    if not args.tag_keys and not args.tag_sets and not args.articles and not args.tagging:
        parser.print_usage()

    session = sessionmaker(bind=models.engine)()

    if args.tag_keys:
        data = csv.reader(args.tag_keys, delimiter='\t')
        header = next(data)
        for row in data:
            k = dict(zip(header, row))
            insert_data(session, k, models.TagKey)

    if args.tag_sets:
        data = csv.reader(args.tag_sets, delimiter='\t')
        header = next(data)
        for row in data:
            k = dict(zip(header, row))
            insert_data(session, k, models.TagSet)

    if args.articles:
        data = csv.reader(args.articles, delimiter='\t')
        header = next(data)
        for row in data:
            k = dict(zip(header, row))
            insert_data(session, k, models.Article)

    if args.tagging:
        data = csv.reader(args.tagging, delimiter='\t')
        header = next(data)
        for row in data:
            k = dict(zip(header, row))
            insert_data(session, k, models.ArticleAndTagSet)

    session.commit()
    session.close()

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    main()
    
