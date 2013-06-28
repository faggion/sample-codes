# coding: utf8

import logging, groumet, sys
from whoosh.index import open_dir
from whoosh.fields import *
from whoosh.qparser import QueryParser

from flask import Flask, request, make_response, render_template

app = Flask(__name__)

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

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.DEBUG)
    app.run(port=5000, debug=True)
