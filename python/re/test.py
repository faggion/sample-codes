# coding: utf-8
import logging, re, sys

def main():
    pat1 = re.compile(r'(https?://[\w/:%#\$&\?\(\)~\.=\+\-]+)')
    test1 = u"abcde aaa あああ ddd http://www.yahoo.co.jp/ いいい zzz ccc http://yahoo.jp";
    print(re.sub(pat1, r'<a href="\1">\1</a>', test1))

if __name__ == '__main__':
    main()
