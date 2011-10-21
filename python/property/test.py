#!/usr/bin/python
# coding:utf-8

class hoge(object):
    def __init__(self):
        self.foo = "foo"
        self.__Testval = u"ほめぱげ"

    def __getattr__(self, name):
        print "no attr: %s" % name
        return None

    def getTestval(self):
        return self.__Testval + u"アクセサ"
    
    def setTestval(self,val):
        print u"Testvalは読み込み専用じゃボケ"
    
    def delTestval(self):
        del self.__Testval
    
    Testval = property(getTestval, setTestval, delTestval)

# インスタンスを使ってみる
if __name__ == '__main__':
    hoge = hoge()
    print hoge.Testval

    hoge.setTestval("foo")
    print hoge.Testval

    hoge.delTestval()

    print hoge.foo
    print hoge.bar
    print hoge.__dict__["foo"]

