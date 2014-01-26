# coding: utf-8

import logging, sys, os
import models
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import or_

def main():
    Session = sessionmaker(bind=models.engine)
    session = Session()

    # - 1つの記事から、その記事が持つタグを全て取り出す
    a = session.query(models.Article).filter(models.Article.id == 1).one()
    for ts in a.tag_sets:
        logging.info("case1: tag_set_id=%d, key=%s, value=%s" % (ts.id, ts.tag_key.name, ts.value))

    session.close()

    # - 1つのタグから、そのタグを持つ記事を全て取り出す
    ts = session.query(models.ArticleAndTagSet).filter(models.ArticleAndTagSet.tag_set_id==8).all()
    for t in ts:
        logging.info("case2: article_id = %d, article_title = %s" % (t.article_id, t.article.title))

    # - 1つの記事から、同じタグを持つ記事を全て取り出す
    a = session.query(models.Article).filter(models.Article.id == 1).one()
    or_cond = []
    for x in a.tag_sets:
        or_cond.append(models.ArticleAndTagSet.tag_set_id == x.id)
    ts = session.query(models.ArticleAndTagSet).filter(models.ArticleAndTagSet.article_id != a.id).filter(or_(*or_cond))
    for t in ts:
        logging.info("case3: article_id = %d, article_title = %s" % (t.article_id, t.article.title))

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    main()
