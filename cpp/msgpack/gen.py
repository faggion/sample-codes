# coding: utf-8
import sys
import msgpack

if __name__ == '__main__':
    data = {"hello":123, "world": [3,2,1] }
    file = open(sys.argv[1], 'wb')
    file.write(msgpack.packb(data))
