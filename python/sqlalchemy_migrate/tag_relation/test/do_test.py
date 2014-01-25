# coding: utf-8

import logging, sys, os
import models
from sqlalchemy.orm import sessionmaker, relationship

def insert_articles(session):
    a1 = models.Article()
    a1.id    = 1
    a1.title = 'test title'
    a1.body  = 'this is test article body'
    session.merge(a1, load=True)

def insert_tag_keys(session):
    tk1 = models.TagKey()
    tk1.id   = 1
    tk1.name = u'area'
    session.merge(tk1, load=True)

    tk2 = models.TagKey()
    tk2.id   = 2
    tk2.name = u'genre'
    session.merge(tk2, load=True)

    tk3 = models.TagKey()
    tk3.id   = 3
    tk3.name = u'tabelog_id'
    session.merge(tk3, load=True)

def insert_tag_sets(session):
    ts1 = models.TagSet()
    ts1.id = 1
    ts1.tag_key_id = 1
    ts1.value = '東京'
    session.merge(ts1, load=True)

    ts2 = models.TagSet()
    ts2.id = 2
    ts2.tag_key_id = 1
    ts2.value = '銀座'
    ts2.parent_id = 1
    session.merge(ts2, load=True)

    ts3 = models.TagSet()
    ts3.id = 3
    ts3.tag_key_id = 1
    ts3.value = '渋谷'
    ts3.parent_id = 1
    session.merge(ts3, load=True)

    ts4 = models.TagSet()
    ts4.id = 4
    ts4.tag_key_id = 1
    ts4.value = '六本木'
    ts4.parent_id = 1
    session.merge(ts4, load=True)

    ts5 = models.TagSet()
    ts5.id = 5
    ts5.tag_key_id = 1
    ts5.value = 'スペイン坂'
    ts5.parent_id = 3
    session.merge(ts5, load=True)

    ts6 = models.TagSet()
    ts6.id = 6
    ts6.tag_key_id = 1
    ts6.value = '道玄坂'
    ts6.parent_id = 3
    session.merge(ts6, load=True)

    # tag_key_id = 2
    ts7 = models.TagSet()
    ts7.id = 7
    ts7.tag_key_id = 2
    ts7.value = 'カレー'
    session.merge(ts7, load=True)

    ts8 = models.TagSet()
    ts8.id = 8
    ts8.tag_key_id = 2
    ts8.value = 'ラーメン'
    session.merge(ts8, load=True)

    # tag_key_id = 3
    ts9 = models.TagSet()
    ts9.id = 9
    ts9.tag_key_id = 3
    ts9.value = 100
    session.merge(ts9, load=True)

    ts10 = models.TagSet()
    ts10.id = 10
    ts10.tag_key_id = 3
    ts10.value = 200
    session.merge(ts10, load=True)

def relate_tags(session):
    at1 = models.ArticleAndTagSet()
    at1.article_id = 1
    at1.tag_set_id = 6
    session.merge(at1, load=True)

    at2 = models.ArticleAndTagSet()
    at2.article_id = 1
    at2.tag_set_id = 8
    session.merge(at2, load=True)

    at3 = models.ArticleAndTagSet()
    at3.article_id = 1
    at3.tag_set_id = 10
    session.merge(at3, load=True)

def main():
    Session = sessionmaker(bind=models.engine)
    session = Session()

    insert_tag_keys(session)
    insert_tag_sets(session)
    insert_articles(session)
    relate_tags(session)

    session.commit()
    session.close()

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    main()
    
