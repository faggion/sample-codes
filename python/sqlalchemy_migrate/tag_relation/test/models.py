# coding: utf-8
import logging, sys, os
#import tables

from sqlalchemy import create_engine, Table, Column, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('mysql://root@localhost/tag_relation',
                       pool_recycle=60,
                       encoding="utf-8")
Base.metadata.bind = engine

class TagKey(Base):
    __table__ = Table('tag_key', Base.metadata, autoload=True)

rel_article_and_tag_set = Table('article_and_tag_set', Base.metadata, autoload=True)

class ArticleAndTagSet(Base):
    __table__ = rel_article_and_tag_set
    article = relationship('Article')
    tag_set = relationship('TagSet')

class Article(Base):
    __table__ = Table('article', Base.metadata, autoload=True)
    tag_sets = relationship('TagSet',
                            secondary=rel_article_and_tag_set)

class TagSet(Base):
    __table__ = Table('tag_set', Base.metadata, autoload=True)
    tag_key = relationship('TagKey')

