# coding: utf-8
import time
import sys
import hashlib
from elixir import *
 
metadata.bind = 'mysql://root@localhost/er_dev'
#metadata.bind.echo = True
 
class User(Entity):
    using_options(tablename='user', autoload=True)
    def foo(self,a):
        return a
    def checkPassword(self,rawpassword):
        sha1 = hashlib.sha1()
        sha1.update(self.salt + rawpassword)
        if self.password == sha1.hexdigest():
            return True
        else:
            return False

if __name__ == '__main__':
    setup_all()
    user = User.query.filter_by(id=8).one()
    print user.hash
    print user.salt
    print user.algorithm
    print user.password
    print User().foo("abc")
    print user.foo("efg")
    if user.checkPassword(sys.argv[1]):
        print "OK"
    else:
        print "NG"
