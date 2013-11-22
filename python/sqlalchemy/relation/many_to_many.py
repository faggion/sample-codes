# coding: utf-8
import logging, sys, os

from sqlalchemy import create_engine, Table, Column, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

engine = create_engine('mysql://root@localhost/test',
                       pool_recycle=60,
                       encoding="utf-8")

association_table = Table('association', Base.metadata,
    Column('left_id', Integer, ForeignKey('left.id')),
    Column('right_id', Integer, ForeignKey('right.id'))
)

class Parent(Base):
    __tablename__ = 'left'
    id = Column(Integer, primary_key=True)
    children = relationship("Child",
                            secondary=association_table)

class Child(Base):
    __tablename__ = 'right'
    id = Column(Integer, primary_key=True)

if __name__ == '__main__':
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)
    #Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    #c1 = Child()
    #c1.id = 1
    #session.merge(c1, load=True)
    #c2 = Child()
    #c2.id = 2
    #session.merge(c2, load=True)
    #c3 = Child()
    #c3.id = 3
    #session.merge(c3, load=True)
    #p = Parent()
    #p.id = 1
    #p.children = [c1, c2, c3]
    #session.merge(p, load=True)

    pp = session.query(Parent).filter(Parent.id == 1).one()
    logging.debug(pp.children)

    session.commit()
    session.close()
