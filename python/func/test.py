# -*- coding: utf-8 -*-

def hoge(foo, bar, baz="DEF"):
    print foo
    print bar
    print baz

def fuga(*params):
    print type(params)
    print params

def moge(a, b, c, d=0):
    print a
    print b
    print c
    print d

def uge(**d):
    print d

# キーワード引数指定
hoge(bar="BBB", foo="AAA")

# 可変長引数関数
a = 1
b = 2
c = 3
fuga(a,b,c)
fuga(a,b)

# 辞書展開関数
#d = {"a":1, "b":2, "c":3, "d":4}
d = {"a":1, "b":2, "c":3}
moge(**d)

#uge(**d)
uge(a=2,b=3)
