from Crypto.Cipher import DES
obj=DES.new('abcdefgh', DES.MODE_ECB)
plain="Guido van Rossum is a space alien."
ciph=obj.encrypt(plain+'XXXXXX')
print obj.decrypt(ciph)
