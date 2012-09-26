# coding: utf-8

t = u'すもももももももものうち'
r = r'すもももももももものうち'

print t
print type(t)
print type(r)
print type(t.encode('utf-8'))

if t[0] == u'す':
    print "OK1"

#if t[0] == 'す': # -> warning
#    print "OK2"

#if r[0] == u'す': # -> warning
#    print "OK3"

if r[0] == r'す': # -> False
    print "OK4" 

