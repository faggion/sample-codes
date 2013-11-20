# coding: utf-8
from sqlalchemy import *
from migrate import *

meta = MetaData()

rtb = Table(
    'rtb', meta,
    Column('id', Integer, primary_key=True),
    mysql_engine='InnoDB',
    sqlite_autoincrement=True)

media = Table(
    'media', meta,
    Column('id',   BigInteger, primary_key=True),
    Column('rate', Integer, default=0),
    mysql_engine='InnoDB',
    sqlite_autoincrement=True)

media_and_rtb = Table(
    'media_and_rtb', meta,
    Column('id',       BigInteger, primary_key=True),
    Column('media_id', BigInteger, ForeignKey("media.id"), nullable=False),
    Column('rtb_id',   Integer,    ForeignKey("rtb.id"), nullable=False),
    mysql_engine='InnoDB',
    sqlite_autoincrement=True)

campaign = Table(
    'campaign', meta,
    Column('id',         BigInteger, primary_key=True),
    Column('media_id',   BigInteger, ForeignKey("media.id")),
    Column('currency',   Integer, default=0),
    Column('priority',   Integer, default=0),
    Column('rank',       Integer, default=0),
    Column('total_goal', BigInteger, nullable=False),
    Column('daily_goal', BigInteger, nullable=False),
    Column('start_at',   BigInteger, nullable=False),
    Column('end_at',     BigInteger, nullable=False),
    Column('total_dig',  BigInteger, default=0),
    Column('daily_dig',  BigInteger, default=0),
    Column('conv',       BigInteger, default=0),
    mysql_engine='InnoDB',
    sqlite_autoincrement=True)

def upgrade(migrate_engine):
    meta.bind = migrate_engine
    rtb.create()
    media.create()
    media_and_rtb.create()
    campaign.create()

def downgrade(migrate_engine):
    meta.bind = migrate_engine
    campaign.drop()
    media_and_rtb.drop()
    media.drop()
    rtb.drop()

