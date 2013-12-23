# coding: utf-8

import logging, random, time
import tanarky.util.sig 
import tanarky.util.caesar
import urllib

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    teststr = 'foo'

    # sig
    sig = tanarky.util.sig.gen(teststr)
    logging.info(sig)
    logging.info(tanarky.util.caesar.encode(sig))
    logging.info(tanarky.util.caesar.raw_encode(sig))

    # caesar
    enc = tanarky.util.caesar.encode(teststr)
    logging.info(enc)
    dec = tanarky.util.caesar.decode(enc)
    logging.info(dec)
    n   = 120
    enc = tanarky.util.caesar.encode(teststr, n)
    logging.info(enc)
    dec = tanarky.util.caesar.decode(enc, n)
    logging.info(dec)

    # NOT normal pattern
    empty = ''
    enc = tanarky.util.caesar.raw_encode(empty, n)
    logging.info('empty raw endoded: (%s)' % enc)
    logging.info('empty sig gen: (%s)' % tanarky.util.sig.gen(empty))
    enc1 = tanarky.util.sig.gen(empty)
    enc2 = tanarky.util.caesar.raw_encode(enc1, n)
    logging.info('empty sig gen raw encoded1: (%s)' % enc1)
    logging.info('empty sig gen raw encoded2: (%s)' % enc2)
    dec1 = tanarky.util.caesar.raw_decode(enc2, n)
    logging.info('empty sig gen raw encoded -> decoded1: (%s)' % dec1)

    ## token
    #a = {"user_uid":1234567890,
    #     "expires_at":1234567890, "scopes":127,
    #     "client_id":"12345678901234567890123456789012"}

    a = {"u":1234567890,
         "e":1234567890, "s":127,
         "c":"12345678901234567890123456789012"}

    #a = {"u":1234567890,
    #     "e":hex(1234567890)[2:], "s":hex(127)[2:],
    #     "c":"12345678901234567890123456789012"}

    ae = urllib.urlencode(a)
    logging.info(len(ae))
    logging.info(ae)

    ac = tanarky.util.caesar.encode(ae)
    logging.info(len(ac))
    logging.info(ac)
    ac = tanarky.util.caesar.encode(ae)
    logging.info(ac)

    #ac20 = tanarky.util.caesar.raw_encode(ae, 20)
    #logging.info(len(ac20))
    #logging.info(ac20)
