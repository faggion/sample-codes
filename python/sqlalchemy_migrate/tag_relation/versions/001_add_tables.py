# coding: utf-8
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from migrate import *

meta = MetaData()

tag_key = Table(
    'tag_key', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(32), nullable=False),
    Column('description', Text, nullable=True),
    mysql_engine='InnoDB',
    sqlite_autoincrement=True)

tag_set = Table(
    'tag_set', meta,
    Column('id', Integer, primary_key=True),
    Column('tag_key_id', Integer, ForeignKey("tag_key.id"), nullable=False),
    Column('value', String(32), nullable=False),
    Column('parent_id', Integer, nullable=True),
    UniqueConstraint('tag_key_id', 'value', name='uniq_1'),
    mysql_engine='InnoDB',
    sqlite_autoincrement=True)

article = Table(
    'article', meta,
    Column('id', Integer, primary_key=True),
    Column('title', String(32), nullable=False),
    Column('body', Text, nullable=False),
    mysql_engine='InnoDB',
    sqlite_autoincrement=True)

article_and_tag_set = Table(
    'article_and_tag_set', meta,
    Column('id', Integer, primary_key=True),
    Column('article_id', Integer, ForeignKey("article.id"), nullable=False),
    Column('tag_set_id', Integer, ForeignKey("tag_set.id"), nullable=False),
    UniqueConstraint('article_id', 'tag_set_id', name='uniq_1'),
    mysql_engine='InnoDB',
    sqlite_autoincrement=True)

def upgrade(migrate_engine):
    meta.bind = migrate_engine
    tag_key.create()
    tag_set.create()
    article.create()
    article_and_tag_set.create()

def downgrade(migrate_engine):
    meta.bind = migrate_engine
    article_and_tag_set.drop()
    article.drop()
    tag_set.drop()
    tag_key.drop()
