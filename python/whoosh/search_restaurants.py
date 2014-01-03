# coding: utf8

import logging, groumet, sys
from whoosh.index import open_dir
from whoosh.fields import *
from whoosh.qparser import QueryParser

from flask import Flask, request, make_response, render_template

app = Flask(__name__)

"""

open_dir は dir内部にある schemaファイルを読み込んでいる(pickleファイル)、あとgenerationファイルも。
ただし、ファイルのチェック(validation)しているだけで、他は何もしていない
更新処理を裏で行うなら、APIはreadonlyでopen_dirするべき
裏でrsyncなどにより反映処理をした時に、どう反映されているかは動作確認が必要

"""

@app.route("/")
def index():
    ix = open_dir("/tmp/groumet_search/")
    T = { "results":[] }
    with ix.searcher() as s:
        query   = QueryParser("stations", ix.schema).parse(u"六本木")
        results = s.search(query)
        for r in results:
            rr = { 'name': r['name'],
                   'thumbnail': r['thumb'],
                   'url':  r['url']}
            T['results'].append(rr)
        logging.debug(T)
        
    return render_template('index.html', T=T)

@app.route("/2")
@open_index
def index2(ix, searcher):
    ix = open_dir("/tmp/groumet_search/")
    T = { "results":[] }
    with ix.searcher() as s:
        query   = QueryParser("stations", ix.schema).parse(u"六本木")
        results = s.search(query)
        for r in results:
            rr = { 'name': r['name'],
                   'thumbnail': r['thumb'],
                   'url':  r['url']}
            T['results'].append(rr)
        logging.debug(T)
        
    return render_template('index.html', T=T)

def open_index(f):
    def wrapper(*args, *kwargs):
        ix = open_dir("/tmp/groumet_search/")
        with ix.searcher() as s:
            return f(ix, s, *args, *kwargs)
    return wrapper

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.DEBUG)
    app.run(port=5000, debug=True)
