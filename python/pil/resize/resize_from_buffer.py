# coding: utf-8

import logging, Image, StringIO

def main():
    #name = 'nozomi'
    name = 'shinoda'
    filename = '%s.jpg' % name
    buf = open(filename, 'rb').read()
    
    im = Image.open(StringIO.StringIO(buf))

    logging.debug(len(buf))
    logging.debug(im.format)
    logging.debug(im.size)
    logging.debug(im.mode)

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    main()
