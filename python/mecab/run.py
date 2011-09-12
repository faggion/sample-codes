# -*- coding: utf-8 -*-
import os
import sys
import random
import MeCab
import wakati

from prettyprint import pp, pp_str

if __name__ == "__main__":
    src = open("test.txt", "r").read()
    wordlist = wakati.parse(src)
    pp(wordlist)
    #ret = wakati.parse("今日は、いい天気ですね。明日はどんな天気でしょうか？")
    #pp(ret)
