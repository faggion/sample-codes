# -*- coding: utf-8 -*-
import os
import sys
import random
import MeCab

from prettyprint import pp, pp_str

def wakati(text):
    t = MeCab.Tagger("-Owakati")
    m = t.parse(text)
    result = m.rstrip(" \n").split(" ")
    return result

if __name__ == "__main__":
    filename = "test.txt"
    src = open(filename, "r").read()
    wordlist = wakati(src)
    #print(wordlist)
    
    # Create table of Markov Chain
    markov = {}
    w1 = w2 = w3 = ""
    for word in wordlist:
        if word == " ":
            continue

        if (w1, w2, w3) not in markov:
            markov[(w1, w2, w3)] = []
        markov[(w1, w2, w3)].append(word)
        w1, w2, w3= w2, w3, word

        if word == "。" or word == "！":
            w1 = w2 = w3 = ""
    
    # Generate Sentence
    count = 1
    sentence = ""

    w1 = w2 = w3 = ""
    while count < len(wordlist):
        count += 1
        mmm = markov.get((w1,w2,w3), False)
        if mmm == False:
            continue
        tmp = random.choice(mmm)
        sentence += tmp
        w1, w2, w3 = w2, w3, tmp

    print sentence
