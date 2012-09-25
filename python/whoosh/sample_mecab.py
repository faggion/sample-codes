# coding: utf8
import MeCab
from whoosh.analysis import Token,Tokenizer
from whoosh.compat import (callable, iteritems, string_type, text_type,
                           integer_types, u, xrange, next)
from whoosh.lang.dmetaphone import double_metaphone
from whoosh.lang.porter import stem
from whoosh.util import lru_cache, unbound_cache, rcompile

STOP_WORDS = frozenset(('a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'can',
                        'for', 'from', 'have', 'if', 'in', 'is', 'it', 'may',
                        'not', 'of', 'on', 'or', 'tbd', 'that', 'the', 'this',
                        'to', 'us', 'we', 'when', 'will', 'with', 'yet',
                        'you', 'your'))

# こっちを修正する必要あり
class MecabTokenizer(Tokenizer):
    """
    Uses a regular expression to extract tokens from text.
    
    >>> rex = RegexTokenizer()
    >>> [token.text for token in rex(u("hi there 3.141 big-time under_score"))]
    ["hi", "there", "3.141", "big", "time", "under_score"]
    """
    def __init__(self):
        #self.tagger = MeCab.Tagger('mecabrc')
        self.tagger = MeCab.Tagger('-Owakati')

    def __call__(self, value, positions=False, chars=False,
                 keeporiginal=False, removestops=True,
                 start_pos=0, start_char=0, mode='', **kwargs):
        assert isinstance(value, text_type), "%r is not unicode" % value
        return self.tagger.parse(value.encode("utf8")).decode('utf8').split(' ')


def MecabAnalyzer(expression=None,
                  stoplist=STOP_WORDS,
                  minsize=2,
                  maxsize=None,
                  gaps=False):
    """Composes a RegexTokenizer with a LowercaseFilter and optional
    StopFilter.
    
    >>> ana = StandardAnalyzer()
    >>> [token.text for token in ana("Testing is testing and testing")]
    ["testing", "testing", "testing"]

    :param expression: The regular expression pattern to use to extract tokens.
    :param stoplist: A list of stop words. Set this to None to disable
        the stop word filter.
    :param minsize: Words smaller than this are removed from the stream.
    :param maxsize: Words longer that this are removed from the stream.
    :param gaps: If True, the tokenizer *splits* on the expression, rather
        than matching on the expression.
    """

    return MecabTokenizer()

MecabAnalyzer.__inittypes__ = dict(expression=text_type, gaps=bool,
                                   stoplist=list, minsize=int, maxsize=int)


mec = MecabAnalyzer()
print [token.text for token in mec(u"今日は天気です")]
print mec(u"今日は天気です")



if __name__ == '__main__':
    from whoosh.index import create_in
    from whoosh.fields import *

    schema = Schema(title=TEXT(stored=True),
                    path=ID(stored=True),
                    content=TEXT(stored=True))

    ix     = create_in("/tmp/", schema)
    writer = ix.writer()

    writer.add_document(title=u"First document",
                        path=u"/a",
                        content=u"This is the first document we've added!")

    writer.add_document(title=u"Second document",
                        path=u"/b",
                        content=u"The second one is even more interesting!")
    writer.commit()

    from whoosh.qparser import QueryParser

    query   = QueryParser("content", ix.schema).parse(u"Even")
    results = ix.searcher().search(query)
    print results[0]
