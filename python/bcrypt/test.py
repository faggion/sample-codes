# coding: utf-8
import logging, os, sys, traceback, base64
from Crypto.Cipher import Blowfish

def PKCS5Padding(string):
    byteNum = len(string)
    packingLength = 8 - byteNum % 8
    appendage = chr(packingLength) * packingLength
    logging.debug("padding char is %s" % ord(chr(packingLength)))
    return string + appendage

def PKCS5Unpadding(string):
    stringlen = len(string)
    c = ord(string[stringlen-1])
    logging.debug("last char is %d" % c)
    return string[0:stringlen-c]

def PandoraEncrypt(string):
    key = b'6#26FRL$ZWD'
    c1  = Blowfish.new(key, Blowfish.MODE_ECB)
    packedString = PKCS5Padding(string)
    logging.debug("packedString len = %d" % len(packedString))
    return c1.encrypt(packedString)

def PandoraDecrypt(string):
    key = b'6#26FRL$ZWD'
    c1  = Blowfish.new(key, Blowfish.MODE_ECB)
    unpacked_str = c1.decrypt(string)
    return unpacked_str

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.DEBUG)

    ## 12 bytes
    #s = 'testingshoge'
    # 8 bytes
    s = b'testings' 
    logging.debug(len(s))
    c = PandoraEncrypt(s)

    encoded_str = base64.b64encode(c)
    logging.debug(encoded_str)
    e = PandoraDecrypt(base64.b64decode(encoded_str))
    logging.debug("'%s'" % PKCS5Unpadding(e))
