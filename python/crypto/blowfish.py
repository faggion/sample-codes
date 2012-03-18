from Crypto.Cipher import Blowfish
import base64

obj = Blowfish.new('abcdefgh', Blowfish.MODE_ECB)

plain="12345678"

#ciph=obj.encrypt(plain+'XXXXXX')
ciph=obj.encrypt(plain)

print base64.b64encode(ciph)
print obj.decrypt(ciph)
