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

---

Group
-------------

- 男女 (男、女、中性)
- 年代（10,20,30,40） -> あんまり意味ないかも
- 購買力（高い、低い、不明）

Userがどこのグループに属するか

定義

購買力＝広告反応力＝広告をクリックするか、特にコマース系広告のクリック率が高いかどうか

まずは購買力の判定？

何の広告をクリックするか、を効率化するために、Frequencyを上げる（同じ広告を2度出さない）
広告に属性スコアを持たせる

30代向け化粧品広告の場合
  男: 0、女: 100、中性: 0
  10代: 0、20代: 20、30代: 70、40代: 10、
  購買力あり: 90、購買力なし: 10

旅行広告主の場合
  男: 30、女: 40、中性: 30
  10代: 20、20代: 20、30代: 20、40代: 20、50代: 20
  購買力あり: 60、購買力なし: 40

グルメメディアの場合
  男: 10、女: 30、中性: 60
  10代: 20、20代: 20、30代: 20、40代: 20、50代: 20
  購買力あり: 20、購買力なし: 80

クリエイティブの集合が広告主のスコアになる
ユーザの集合がメディアのスコアになる

まずは、広告的に尖ったものを出して、該当するか否かを判定していくのがよいと思われる


一方、何の広告をクリックするか以外にUser判定方法はないのか？


---

User  * Media
Media * Advertiser
User  * Advertiser
User  * Creative
Category * Category

1. どうやって最適化するか

a. どういうカテゴリツリーにするか、どうやってメンテナンスしていくか

- Media

  - グルメ、東京、レストラン、カキフライ

- Creative

  - 東京、旅行、ホテル
  - クーポン、エステ、東京
  - 化粧品、送料無料
  - ドラクエ、ゲーム、アプリ
















"""


