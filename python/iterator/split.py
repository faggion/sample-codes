# coding: utf8
import re, MeCab
from whoosh.util import lru_cache, unbound_cache, rcompile

class Token(object):
    def __init__(self,
                 positions=False,
                 chars=False,
                 removestops=True,
                 mode='',
                 **kwargs):
        self.positions = positions
        self.chars = chars
        self.stopped = False
        self.boost = 1.0
        self.removestops = removestops
        self.mode = mode
        self.__dict__.update(kwargs)

class MyTokenizer():
    def __init__(self, expression="[^/]+"):
        self.expr = rcompile(expression, re.UNICODE)

    def __call__(self, value, mode='', **kwargs):
        assert isinstance(value, unicode), "%r is not unicode" % value
        #print kwargs
        token = Token(**kwargs)
        #print token
        self.tagger = MeCab.Tagger('-Owakati')
        self.tagger = MeCab.Tagger('mecabrc')
        result = self.tagger.parse(value.encode("utf8")).decode('utf8')

        #cur = 0
        for match in re.compile("(\S+)\s+(\S+)\n").finditer(result):
            category = match.group(2).split(",")
            if 0 < len(category) and \
                    (category[0] == u'名詞' or category[0] == u'動詞' \
                         or category[0] == u'形容詞' or category[0] == u'副詞'):
                token.text = match.group(1)
                print "%d, %d : %s" % (match.start(), match.end(), match.group(1))
                #print "%s" % (match.group(0)[int(match.start()):int(match.end())])
                #token.pos = cur
                yield token
            #cur += len(match.group(1))

#test = u'今日はよく晴れた天気で気持ちいいですね？'
test = u'東京都世田谷区千歳台'
m = MyTokenizer()
for x in m(test):
    pass
    #print x.text
