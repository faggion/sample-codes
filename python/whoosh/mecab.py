# coding: utf8
import MeCab,re
from whoosh.analysis import Token,Tokenizer,RegexTokenizer

class MeCabTokenizer(Tokenizer):
    __inittypes__ = dict(expression=unicode, gaps=bool)

    def __call__(self, value, mode='', positions=False, **kwargs):
        assert isinstance(value, unicode), "%r is not unicode" % value
        token = Token(**kwargs)
        tagger = MeCab.Tagger('mecabrc')
        result = tagger.parse(value.encode("utf8")).decode('utf8')

        cur = 0
        for match in re.compile("(\S+)\s+(\S+)\n").finditer(result):
            category = match.group(2).split(",")
            if 0 < len(category) and \
                    (category[0] == u'名詞' or category[0] == u'動詞' \
                         or category[0] == u'形容詞' or category[0] == u'副詞'):
                token.text = match.group(1)
                token.pos  = cur
                yield token
            cur += len(match.group(1))

def MeCabAnalyzer(expression=r"(\S+)\s+(\S+)\n", stoplist=None, minsize=2, maxsize=None, gaps=False):
    return MeCabTokenizer()
MeCabAnalyzer.__inittypes__ = dict(expression=unicode, gaps=bool, stoplist=list, minsize=int, maxsize=int)
