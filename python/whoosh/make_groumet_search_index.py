# coding: utf8

import logging, groumet, sys
from whoosh.index import create_in
from whoosh.fields import *

def build_index(w, data):
    try:
        w.add_document(name=unicode(d['n']),
                       thumb=d['th'],
                       rate_avr=float(d['ravr']),
                       lat=float(d['lat']),
                       lon=float(d['lon']),
                       stations=unicode(d['st']),
                       categories=unicode(d['cat']),
                       url=d['u'])
    except:
        pass

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.DEBUG)
    ix     = create_in("/tmp/groumet_search/", groumet.schema)
    writer = ix.writer()

    for data in iter(sys.stdin.readline, ""):
        d = {}

        for dd in data.rstrip().split("\t"):
            try:
                kv = dd.split(":", 1)
                d[kv[0]] = kv[1].decode("utf-8")
            except:
                logging.debug(data)
                pass
        build_index(writer, d)
    writer.commit()



