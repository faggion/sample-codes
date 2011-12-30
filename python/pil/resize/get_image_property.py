# coding: utf-8

import logging, sys, Image

def main(name):
    im = Image.open(name)
    logging.debug(im.format)
    logging.debug(im.size)
    logging.debug(im.mode)

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    main(sys.argv[1])
