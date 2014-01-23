# coding: utf-8
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from migrate import *

meta = MetaData()

tag_key = Table(
    'tag_key', meta,
    Column('id', Integer, primary_key=True),
    Column('key_name', String(32), nullable=False),
    mysql_engine='InnoDB',
    sqlite_autoincrement=True)

def upgrade(migrate_engine):
    meta.bind = migrate_engine
    tag_key.create()

def downgrade(migrate_engine):
    meta.bind = migrate_engine
    tag_key.drop()
