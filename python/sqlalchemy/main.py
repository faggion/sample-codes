# coding: utf-8
import logging, sys, os

from sqlalchemy import create_engine
engine = create_engine('mysql://root@localhost/test', echo=True,pool_recycle=60, encoding="utf-8" )
#engine = create_engine('sqlite:///:memory:', echo=True)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String, Boolean
class User(Base):
    __tablename__  = 'users'
    __table_args__ = {'mysql_engine': 'InnoDB'} 

    # mysqlの場合自動でauto_incrementになる、sqliteにはauto_incrementがない？のでつかない
    id       = Column(Integer, primary_key=True)
    name     = Column(String(32), unique=True)
    fullname = Column(String(64), index=True)
    password = Column(String(16))
    is_male  = Column(Boolean())

    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
       return "<User('%s','%s', '%s', '%s')>" % (self.name, self.fullname, self.password, self.is_male)

class User2(Base):
    __tablename__  = 'users'
    __table_args__ = {'autoload': True} 

    def __repr__(self):
       return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    #ret = engine.execute("select 1").scalar()
    #logging.debug(ret)
    #logging.debug(sys.argv)
    Base.metadata.create_all(engine)
    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()
    for i in session.query(User).filter(User.name=='satoshi').all():
        logging.debug(i)
        logging.debug(i.is_male)

"""

- alter tableはどうする？ -> sqlalchemy-migrate パッケージを使うべし
- unique key, indexをつけるには？ -> Column(*, index=True, unique=True)
- select for udpate -> s = table.select(table.c.user=="test",for_update=True)
                       http://stackoverflow.com/questions/10081121/sqlalchemy-select-for-update-example

"""
