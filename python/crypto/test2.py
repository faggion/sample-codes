from Crypto.PublicKey import RSA
from Crypto import Random
import base64

random_generator = Random.new().read
key = RSA.generate(1024, random_generator)
#key = RSA.generate(2048, random_generator)

print key.can_encrypt()
print key.can_sign()
print key.has_private()

text = "12345678"
#text = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab'
public_key = key.publickey()
enc_data = public_key.encrypt(text, 32)

#print enc_data
print base64.b64encode(str(enc_data))
print key.decrypt(enc_data)
