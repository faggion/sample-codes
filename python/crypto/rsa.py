# -*- coding: utf-8 -*-

"""
openssl genrsa -out privkey_rsa.pem 8196
openssl rsa -pubout -in privkey_rsa.pem -out pubkey_rsa.pem

8196 -> 1024 bytesまで
4096 ->  512 bytesまで
2048 ->  256 bytesまで
1024 ->  128 bytesまで

"""

import base64
import Crypto.PublicKey.RSA
import Crypto.Util.randpool

pool = Crypto.Util.randpool.RandomPool()

## RSAオブジェクトをランダムな鍵で生成する
#rsa = Crypto.PublicKey.RSA.generate(2048, pool.get_bytes)
#pub_rsa = rsa.publickey()
pub_rsa = Crypto.PublicKey.RSA.importKey(open('pubkey_rsa.pem', 'r').read())

# RSAオブジェクトをタプルから生成する
# rsa.nが公開鍵、rsa.dが秘密鍵と思う
#priv_rsa = Crypto.PublicKey.RSA.construct((rsa.n, rsa.e, rsa.d))
priv_rsa = Crypto.PublicKey.RSA.importKey(open('privkey_rsa.pem', 'r').read())

# 暗号化する
org = '123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890'
enc = pub_rsa.encrypt(org, "")

# 復号する
dec = priv_rsa.decrypt(enc)
#print enc[0]
dec = priv_rsa.decrypt(base64.b64decode(base64.b64encode(str(enc[0]))))

#print "private: n=%d, e=%d, d=%d, p=%d, q=%d, u=%d" % \
#      (rsa.n, rsa.e, rsa.d, rsa.p, rsa.q, rsa.u)
#print "public: n=%d, e=%d" % (pub_rsa.n, pub_rsa.e)
#print "encrypt:", enc
print "encrypt:", base64.b64encode(str(enc))
print "decrypt:", dec

# 署名する
text = "hello"
signature = priv_rsa.sign(text, "")
# 文字列が変わってないか調べる
print pub_rsa.verify(text, signature)
print pub_rsa.verify(text+"a", signature)
