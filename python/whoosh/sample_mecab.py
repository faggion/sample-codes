# coding: utf8
from mecab import MeCabAnalyzer
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.query  import *
from whoosh.qparser import QueryParser

if __name__ == '__main__':

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
