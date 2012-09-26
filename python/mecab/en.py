#coding:utf-8
import MeCab,sys,re
from whoosh.util import rcompile

test_sentence = u'satoshi.tanaka'

if isinstance(test_sentence, unicode):
    test_sentence = test_sentence.encode('utf8')

tagger = MeCab.Tagger('mecabrc')
result = tagger.parse(test_sentence)
print result
result = result.decode('utf8')
print "--------"
for match in re.compile("(\S+)\s+(\S+)\n").finditer(result):
    category = match.group(2).split(",")
    if category[0] == u'名詞' or category[0] == u'動詞' or category[0] == u'形容詞' or category[0] == u'副詞':
        print '"%s" -> "%s"' % (match.group(1), match.group(2))
