# coding: utf-8
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine  = create_engine('mysql://root@localhost/adv4', encoding="utf-8", pool_recycle=60)
Session = sessionmaker(bind=engine)
#conn = engine.connect()

