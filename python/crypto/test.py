# coding: utf-8

"""
openssl genrsa -out privkey_rsa.pem 1024
openssl rsa -pubout -in privkey_rsa.pem -out pubkey_rsa.pem
"""

from Crypto.PublicKey import RSA
import base64

#pool = Crypto.Util.randpool.RandomPool()
#rsa  = Crypto.PublicKey.RSA.generate(1024, pool.get_bytes)
 
pub  = RSA.importKey(open('pubkey_rsa.pem', 'r').read())
priv = RSA.importKey(open('privkey_rsa.pem', 'r').read())
 
text = '12345678'
#text = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
print text

#crypto = pub.encrypt(text, '')
crypto = pub.encrypt(text, 1024)
crypto_enc = base64.b64encode(str(crypto))
print crypto_enc
print priv.decrypt(crypto)

