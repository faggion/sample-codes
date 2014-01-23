# coding: utf-8
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from migrate import *

meta = MetaData()

media = Table(
    'media', meta,
    Column('id', BigInteger, primary_key=True),
    #Column('width',  Integer, nullable=False),
    #UniqueConstraint('width', 'height', name='adsize'),
    mysql_engine='InnoDB',
    sqlite_autoincrement=True)

advertiser = Table(
    'advertiser', meta,
    Column('id', BigInteger, primary_key=True),
    mysql_engine='InnoDB',
    sqlite_autoincrement=True)

media_config = Table(
    'media_config', meta,
    Column('id', Integer, primary_key=True),
    Column('media_id',      BigInteger, ForeignKey("media.id"), nullable=False),
    Column('advertiser_id', BigInteger, ForeignKey("advertiser.id"), nullable=False),
    Column('conf', Text),
    UniqueConstraint('media_id', 'advertiser_id', name='maa'),
    mysql_engine='InnoDB',
    sqlite_autoincrement=True)

creative = Table(
    'creative', meta,
    Column('id', BigInteger, primary_key=True),
    Column('advertiser_id', BigInteger, ForeignKey("advertiser.id"), nullable=False),
    Column('conf', Text, nullable=False),
    mysql_engine='InnoDB',
    sqlite_autoincrement=True)

def upgrade(migrate_engine):
    meta.bind = migrate_engine
    media.create()
    advertiser.create()
    media_config.create()
    creative.create()

def downgrade(migrate_engine):
    meta.bind = migrate_engine

    creative.drop()
    media_config.drop()
    advertiser.drop()
    media.drop()
