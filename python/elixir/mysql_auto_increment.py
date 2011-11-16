# coding: utf-8
import time
import sys
from elixir import *
 
metadata.bind = 'mysql://flask@192.168.158.130/er_dev'
metadata.bind.echo = True
 
## booksテーブルにマッピングするオブジェクト
#class Book(Entity):
#  using_options(tablename='books', autoload=True)

class Test(Entity):
#  using_options(tablename='tests', autoload=True)
  using_options(tablename='tests')

def main():
  time.sleep(3)
  setup_all()
  time.sleep(3)
  ## insert 
  #try:
  #  t1 = Test(title='1Q84')
  #  t2 = Test(title='リアル9')
  #  session.commit()
  #except:
  #  print sys.exc_info()
  #session.close()
  #
  ## select
  #for b in Test.query.all():
  #  print b
 
if __name__ == '__main__':
  main()
