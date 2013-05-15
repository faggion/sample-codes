# coding: utf-8

def plus(a):
    return a + 10;

def double(a):
    return a * a

def echo(func_name, num):
    #import foo
    #methodToCall = getattr(foo, 'bar')
    #methodToCall()
    print("value is %d" % globals()[func_name](num))
    #print(globals())

echo("plus", 100)
echo("double", 20)
