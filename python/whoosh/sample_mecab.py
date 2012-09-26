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

if __name__ == '__main__':
    from whoosh.index import create_in
    from whoosh.fields import *
    from whoosh.query  import *

    # MeCabAnalyzerテスト
    mec = MeCabAnalyzer()
    for i in [token.text for token in mec(u"今日は天気です")]:
        print i

    print "--------"

    # MeCabAnalyzerを使ってIndexing
    schema = Schema(title=TEXT(stored=True, analyzer=MeCabAnalyzer()),
                    path=ID(stored=True),
                    content=TEXT(stored=True, analyzer=MeCabAnalyzer()))

    # 先にディレクトリを作っとかないと怒られる
    ix     = create_in("/tmp/mecab", schema)
    writer = ix.writer()

    writer.add_document(title=u"this is first document.",
                        path=u"/b",
                        content=u"i am a programmer. he is dentist.")
    writer.add_document(title=u"これが2個目のドキュメントかな",
                        path=u"/b",
                        content=u"北海道札幌市千歳区")
    writer.commit()

    from whoosh.qparser import QueryParser

    searcher = ix.searcher()
    try:
        #query   = QueryParser("content", ix.schema).parse(u"北海道")
        #query   = QueryParser("title", ix.schema).parse(u"ドキュメント")
        #query   = And([Term("title", u"ドキュメント"), Term('content', u"千歳")])
        query   = Or([Term("title", u"ドキュメント"), Term('content', u"programmer")])
        results = searcher.search(query)
        for r in results:
            print r['title']
    finally:
        searcher.close()
