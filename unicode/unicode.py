uni = u'{"foo":"\u30af\u30ea\u30ce\u30c3\u30da"}'

print uni.encode('utf-8')

uni = '{"foo":"\u30af\u30ea\u30ce\u30c3\u30da"}'
print uni.decode('unicode-escape')
