# coding: utf-8
import logging, sys, os

from sqlalchemy import create_engine, Table, Column, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

engine = create_engine('mysql://root@localhost/cpaopt',
                       pool_recycle=60,
                       encoding="utf-8")

Base.metadata.bind = engine

class MediaConfig(Base):
    __table__ = Table('media_config', Base.metadata, autoload=True)

class Media(Base):
    __table__ = Table('media', Base.metadata, autoload=True)
    configs = relationship("MediaConfig")

class Advertiser(Base):
    __table__ = Table('advertiser', Base.metadata, autoload=True)

class Creative(Base):
    __table__ = Table('creative', Base.metadata, autoload=True)
    advertiser = relationship("Advertiser")

def insert_adv_and_media(session):
    a1 = Advertiser()
    a1.id = 1
    session.merge(a1, load=True)

    a2 = Advertiser()
    a2.id = 2
    session.merge(a2, load=True)

    a3 = Advertiser()
    a3.id = 3
    session.merge(a3, load=True)

    m1 = Media()
    session.add(m1)
    session.commit()

    logging.debug(m1.id)

def insert_creatives(session):
    #a1 = Advertiser()
    #session.add(a1)

    cr1 = Creative()
    cr1.advertiser_id = 2
    cr1.conf = "this is creative 1"
    session.add(cr1)
    session.commit()
    logging.debug(cr1.id)

def search(session, media_id):
    session.query(Creative).filter(.id == _id)

if __name__ == '__main__':
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)

    Session = sessionmaker(bind=engine)
    session = Session()
    #insert_adv_and_media(session)
    #insert_creatives(session)
    session.close()

"""

Phase1
mysql> select mc.advertiser_id from media as m left join media_config as mc on mc.media_id = m.id where m.id = 1;

これでmediaを抽出してから（本当は order by score ＋ クリック済み advertiserを除外して）、advertierを1つ決定。

score = 平均注文単価 * アフィリエイト料率 * CVR

User*AdvertiserカテゴリマッチによるCVRはどうやって考慮する？
Media*AdvertiserカテゴリマッチによるCVRはどうやって考慮する？

Phase2

mysql> select * from creative where advertiser_id = 1;

でクリエイティブを抽出、User+Creativeカテゴリマッチ・全体CTR考慮

"""


