# coding: utf-8
from sqlalchemy import *
from migrate import *

def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    camp = Table('campaign', meta, autoload=True)
    col_synced_at = Column('synced_at', BigInteger, default=0)
    col_synced_at.create(camp)

def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    camp = Table('campaign', meta, autoload=True)
    camp.c.synced_at.drop()


