# coding: utf-8

import logging,sys,glob,ctypes

## debian6 only
#_libc = ctypes.CDLL('/lib/libc.so.6')

# mac only
_libc = ctypes.CDLL('/usr/lib/libc.dylib')

if __name__ == '__main__':
    print _libc.printf
    if 1 < len(sys.argv):
        _libc.printf(" ".join(sys.argv[1:]) + "\n")
