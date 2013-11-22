# coding: utf-8
import logging, sys, os, traceback

from sqlalchemy import create_engine, Table
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

import helpers

Base = declarative_base()
Base.metadata.bind = helpers.engine

class Space(Base):
    __table__ = Table('spaces', Base.metadata, autoload=True)
    @classmethod
    def find_by_id(cls, session, _id):
        return session.query(cls).filter(cls.id == _id).one()

class MediaAndRtb(Base):
    __table__ = Table('medias_and_rtbs', Base.metadata, autoload=True)

class Rtb(Base):
    __table__ = Table('rtbs', Base.metadata, autoload=True)
    @classmethod
    def find_by_id(cls, session, _id):
        return session.query(cls).filter(cls.id == _id).one()

class Media(Base):
    __table__ = Table('medias', Base.metadata, autoload=True)
    rtbs = relationship("Rtb", secondary=MediaAndRtb.__table__)
    @classmethod
    def find_by_id(cls, session, _id):
        return session.query(cls).filter(cls.id == _id).one()

class Slot(Base):
    __table__ = Table('slots', Base.metadata, autoload=True)
    @classmethod
    def find_by_id(cls, session, _id):
        return session.query(cls).filter(cls.id == _id).one()

"""

#tbl_media_and_rtb = Table('medias_and_rtbs', Base.metadata, autoload=True)
#class Rtb(Base):
#    __table__ = Table('rtbs', Base.metadata, autoload=True)
#    @classmethod
#    def find_by_id(cls, session, _id):
#        return session.query(cls).filter(cls.id == _id).one()
#class Media(Base):
#    __table__ = Table('medias', Base.metadata, autoload=True)
#    rtbs = relationship("Rtb", secondary=tbl_media_and_rtb)
#    @classmethod
#    def find_by_id(cls, session, _id):
#        return session.query(cls).filter(cls.id == _id).one()

class MediaAndRtb(Base):
    __table__ = Table('medias_and_rtbs', Base.metadata, autoload=True)
    rtb = relationship("Rtb")
class Rtb(Base):
    __table__ = Table('rtbs', Base.metadata, autoload=True)
    @classmethod
    def find_by_id(cls, session, _id):
        return session.query(cls).filter(cls.id == _id).one()
class Media(Base):
    __table__ = Table('medias', Base.metadata, autoload=True)
    rtbs = relationship("MediaAndRtb")
    @classmethod
    def find_by_id(cls, session, _id):
        return session.query(cls).filter(cls.id == _id).one()

"""
