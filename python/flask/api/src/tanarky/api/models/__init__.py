# coding: utf-8
import logging, sys, os, traceback

from sqlalchemy import create_engine, Table
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

import tanarky.api.helpers

Base = declarative_base()
Base.metadata.bind = tanarky.api.helpers.engine

class Media(Base):
    __table__ = Table('media', Base.metadata, autoload=True)

class Adsize(Base):
    __table__ = Table('adsize', Base.metadata, autoload=True)
