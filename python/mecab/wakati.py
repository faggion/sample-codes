# -*- coding: utf-8 -*-
import MeCab
import re, pprint

def parse(text):
    t = MeCab.Tagger("-Owakati")
    #t = MeCab.Tagger()
    m = t.parse(text)
    return m
    #result = m.rstrip(" \n").split(" ")
    #return result
