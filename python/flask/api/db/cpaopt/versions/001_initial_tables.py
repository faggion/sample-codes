# coding: utf-8
from sqlalchemy import *
from migrate import *

meta = MetaData()

media = Table(
    'media', meta,
    Column('id',   Integer, primary_key=True),
    Column('name', String(32), nullable=False),
    mysql_engine='InnoDB',
    sqlite_autoincrement=True)

advertiser = Table(
    'advertiser', meta,
    Column('id',   Integer,    primary_key=True),
    Column('name', String(32), nullable=False),
    mysql_engine='InnoDB',
    sqlite_autoincrement=True)

adsize = Table(
    'adsize', meta,
    Column('id',   Integer, primary_key=True),
    Column('width', Integer, nullable=False),
    Column('height', Integer, nullable=False),
    UniqueConstraint('width', 'height', name='width_and_height'),
    mysql_engine='InnoDB',
    sqlite_autoincrement=True)

media_config = Table(
    'media_config', meta,
    Column('id', Integer, primary_key=True),
    Column('media_id', Integer, ForeignKey("media.id"), nullable=False),
    Column('advertiser_id', Integer, ForeignKey("advertiser.id"), nullable=False),
    Column('conf', Text),
    UniqueConstraint('media_id', 'advertiser_id', name='media_and_adv'),
    mysql_engine='InnoDB',
    sqlite_autoincrement=True)

slot = Table(
    'slot', meta,
    Column('id', Integer, primary_key=True),
    Column('media_id', Integer, ForeignKey("media.id"), nullable=False),
    Column('adsize_id', Integer, ForeignKey("adsize.id"), nullable=False),
    mysql_engine='InnoDB',
    sqlite_autoincrement=True)

creative = Table(
    'creative', meta,
    Column('id', Integer, primary_key=True),
    Column('advertiser_id', Integer, ForeignKey("advertiser.id"), nullable=False),
    Column('conf', Text, nullable=False),
    mysql_engine='InnoDB',
    sqlite_autoincrement=True)

def upgrade(migrate_engine):
    meta.bind = migrate_engine

    media.create()
    advertiser.create()
    adsize.create()
    media_config.create()
    slot.create()
    creative.create()

def downgrade(migrate_engine):
    meta.bind = migrate_engine

    creative.drop()
    slot.drop()
    media_config.drop()
    adsize.drop()
    advertiser.drop()
    media.drop()
