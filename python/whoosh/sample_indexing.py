# coding: utf8
import sys
from mecab import MeCabAnalyzer
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.query  import *
from whoosh.qparser import QueryParser

if __name__ == '__main__':
    mec    = MeCabAnalyzer()
    schema = Schema(path=ID(stored=True),
                    content=TEXT(stored=True, analyzer=MeCabAnalyzer()))
    # 先にディレクトリを作っとかないと怒られる
    ix     = create_in("/tmp/mis", schema)
    writer = ix.writer()

    for line in open('/tmp/a.log', 'r'):
        l = line.split("\t")
        print "%s -> %s" % (l[0], l[1])

        writer.add_document(path=l[0].decode('utf8'), content=l[1].decode('utf8'))

    writer.commit()

    searcher = ix.searcher()
    try:
        print "search words = '%s'" % sys.argv[1]
        query   = QueryParser("content", ix.schema).parse(sys.argv[1].decode('utf8'))
        results = searcher.search(query)
        print "--------"
        for r in results:
            print r['content']

    finally:
        searcher.close()
