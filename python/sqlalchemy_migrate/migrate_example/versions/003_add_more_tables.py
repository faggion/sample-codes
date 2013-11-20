# coding: utf-8
from sqlalchemy import *
from migrate import *

meta = MetaData()
space = Table(
    'space', meta,
    Column('id',     BigInteger, primary_key=True),
    Column('parent', BigInteger, default=0),
    mysql_engine='InnoDB',
    sqlite_autoincrement=True)

def upgrade(migrate_engine):
    meta.bind = migrate_engine
    space.create()

def downgrade(migrate_engine):
    meta.bind = migrate_engine
    space.drop()

