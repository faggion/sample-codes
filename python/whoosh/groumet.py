# coding: utf-8

import logging
from whoosh.index import create_in
from whoosh.fields import *

schema = Schema(name=TEXT(stored=True),
                thumb=TEXT(stored=True),
                rate_avr=NUMERIC(stored=True),
                lat=NUMERIC(stored=True),
                foo=TEXT(stored=True),
                lon=NUMERIC(stored=True),
                categories=KEYWORD(stored=True, commas=True),
                stations=KEYWORD(stored=True, commas=True),
                url=ID(stored=True, unique=True))

