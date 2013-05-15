# coding: utf-8
from sqlalchemy import create_engine,text,exc

#conn = create_engine("mysql://root@localhost/er_dev",
#                     pool_recycle=60,
#                     encoding='utf8')
conn = create_engine("mysql://root@localhost/test",
                     pool_recycle=60,
                     encoding='utf8')


