# coding: utf-8

import logging, Image

def main():
    #name = 'shinoda'
    name = 'nozomi'
    filename = '%s.jpg' % name
    thumbname = '%s_thumbnail.jpg' % name
    im = Image.open(filename)
    logging.debug(im.format)
    logging.debug(im.size)
    logging.debug(im.mode)
    #im.thumbnail((400,300), Image.ANTIALIAS)
    im.thumbnail(size=(400,300))
    im.save(thumbname, 'JPEG')

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    main()
