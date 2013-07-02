# coding: utf8

from whoosh.index import create_in
from whoosh.fields import *

schema = Schema(title=TEXT(stored=True),
                path=ID(stored=True),
                price=NUMERIC(stored=True),
                tag=TEXT(stored=True),
                content=TEXT(stored=True))

ix     = create_in("/tmp/", schema)
writer = ix.writer()

writer.add_document(title=u"First document",
                    path=u"/a",
                    price=int("3"),
                    tag=u"Tokyo",
                    content=u"This is the first document we've added!")

writer.add_document(title=u"Second document",
                    path=u"/b",
                    content=u"The second one is even more interesting!")

third = { "title":   u"Third document",
          "path":    u"/c",
          "price":   1200,
          "content": u"This is third document, it's amazing!" }
writer.add_document(**third)

writer.commit()

from whoosh.qparser import QueryParser

#with ix.searcher() as searcher:
#    query = QueryParser("content", ix.schema).parse(u"first")
#    results = searcher.search(query)
#    print dict(results[0])
#query   = QueryParser("content", ix.schema).parse(u"Even")
#query   = QueryParser("title", ix.schema).parse(u"first")
query   = QueryParser("title", ix.schema).parse(u"third")

aaa = ix.searcher()
results = aaa.search(query)
print results[0]
