# coding: utf-8
from sqlalchemy import *
from migrate import *

meta = MetaData()

spaces = Table(
    'spaces', meta,
    Column('id',     BigInteger, primary_key=True),
    Column('parent', BigInteger, default=0),
    mysql_engine='InnoDB',
    sqlite_autoincrement=True)

rtbs = Table(
    'rtbs', meta,
    Column('id', Integer, primary_key=True),
    mysql_engine='InnoDB',
    sqlite_autoincrement=True)

medias = Table(
    'medias', meta,
    Column('id',   BigInteger, primary_key=True),
    Column('rate', Integer, default=0),
    mysql_engine='InnoDB',
    sqlite_autoincrement=True)

slots = Table(
    'slots', meta,
    Column('id',       BigInteger, primary_key=True),
    Column('space_id', BigInteger, ForeignKey("spaces.id"), nullable=False),
    Column('media_id', BigInteger, ForeignKey("medias.id"), nullable=False),
    mysql_engine='InnoDB',
    sqlite_autoincrement=True)

medias_and_rtbs = Table(
    'medias_and_rtbs', meta,
    Column('id',       BigInteger, primary_key=True),
    Column('media_id', BigInteger, ForeignKey("medias.id"), nullable=False),
    Column('rtb_id',   Integer,    ForeignKey("rtbs.id"), nullable=False),
    UniqueConstraint('media_id', 'rtb_id', name='media_rdb'),
    mysql_engine='InnoDB',
    sqlite_autoincrement=True)

# adcreative
adcreatives = Table(
    'adcreatives', meta,
    Column('id',            BigInteger, primary_key=True),
    Column('banner_id',     Integer, nullable=False),
    Column('https_enabled', Boolean, default=False),
    Column('conf',          Text, nullable=False),
    Column('crc32',         BigInteger, nullable=False),
    UniqueConstraint('banner_id', 'crc32', name='adc'),
    mysql_engine='InnoDB',
    sqlite_autoincrement=True)

# adgroup
adgroups = Table(
    'adgroups', meta,
    Column('id',        BigInteger, primary_key=True),
    Column('weight',    Integer,    nullable=False),
    Column('adcreative_id', BigInteger, ForeignKey("adcreatives.id"), nullable=False),
    mysql_engine='InnoDB',
    sqlite_autoincrement=True)

# estimation
estimations = Table(
    'estimations', meta,
    Column('id',    BigInteger, primary_key=True),
    Column('crc32', BigInteger, nullable=False),
    Column('body',  Text, nullable=False),
    UniqueConstraint('crc32', name='idx'),
    mysql_engine='InnoDB',
    sqlite_autoincrement=True)

# constraint
constraints = Table(
    'constraints', meta,
    Column('id',    BigInteger, primary_key=True),
    Column('crc32', BigInteger, nullable=False),
    Column('body',  Text, nullable=False),
    UniqueConstraint('crc32', name='idx'),
    mysql_engine='InnoDB',
    sqlite_autoincrement=True)

# trigger
triggers = Table(
    'triggers', meta,
    Column('id',    BigInteger, primary_key=True),
    Column('crc32', BigInteger, nullable=False),
    Column('body',  Text, nullable=False),
    UniqueConstraint('crc32', name='idx'),
    mysql_engine='InnoDB',
    sqlite_autoincrement=True)

campaigns = Table(
    'campaigns', meta,
    Column('id',         BigInteger, primary_key=True),
    Column('start_at',   BigInteger, nullable=False),
    Column('end_at',     BigInteger, nullable=False),
    Column('media_id',   BigInteger, ForeignKey("medias.id")),
    Column('currency',   Integer, default=0),
    Column('priority',   Integer, default=0),
    Column('rank',       Integer, default=0),
    Column('total_goal', BigInteger, nullable=False),
    Column('daily_goal', BigInteger, nullable=False),
    Column('total_dig',  BigInteger, default=0),
    Column('daily_dig',  BigInteger, default=0),
    Column('synced_at',  BigInteger, default=0),
    Column('conv',       BigInteger, default=0),
    mysql_engine='InnoDB',
    sqlite_autoincrement=True)

schedules = Table(
    'schedules', meta,
    Column('id',            BigInteger, primary_key=True),
    Column('start_at',      BigInteger, nullable=False),
    Column('end_at',        BigInteger, nullable=False),
    Column('type',          Integer, default=0),
    Column('price',         BigInteger, nullable=False),
    Column('campaign_id',   BigInteger, ForeignKey("campaigns.id"), nullable=False),
    Column('space_id',      BigInteger, ForeignKey("spaces.id"), nullable=False),
    Column('adsize_id',     Integer, default=0),
    Column('constraint_id', BigInteger, ForeignKey("constraints.id"), default=0),
    Column('estimation_id', BigInteger, ForeignKey("estimations.id"), default=0),
    Column('trigger_id',    BigInteger, ForeignKey("triggers.id"), default=0),
    mysql_engine='InnoDB',
    sqlite_autoincrement=True)

schedules_and_adgroups = Table(
    'schedules_and_adgroups', meta,
    Column('id',          BigInteger, primary_key=True),
    Column('schedule_id', BigInteger, ForeignKey("schedules.id"), nullable=False),
    Column('adgroup_id',  BigInteger, ForeignKey("adgroups.id"),  nullable=False),
    UniqueConstraint('schedule_id', 'adgroup_id', name='sche_and_adg'),
    mysql_engine='InnoDB',
    sqlite_autoincrement=True)

def upgrade(migrate_engine):
    meta.bind = migrate_engine

    spaces.create()
    rtbs.create()
    medias.create()
    slots.create()
    medias_and_rtbs.create()
    adcreatives.create()
    adgroups.create()
    estimations.create()
    constraints.create()
    triggers.create()
    campaigns.create()
    schedules.create()
    schedules_and_adgroups.create()

def downgrade(migrate_engine):
    meta.bind = migrate_engine

    schedules_and_adgroups.drop()
    schedules.drop()
    campaigns.drop()
    triggers.drop()
    constraints.drop()
    estimations.drop()
    adgroups.drop()
    adcreatives.drop()
    medias_and_rtbs.drop()
    slots.drop()
    medias.drop()
    rtbs.drop()
    spaces.drop()
