# coding: utf-8
import logging, os, sys, traceback, argparse
from amazonproduct import API
from lxml import etree

def search():
    api = API(locale='jp')
    #total_results = node.Items.TotalResults.pyval
    #total_pages = node.Items.TotalPages.pyval
    for book in api.item_search('Books', Publisher=u'村上'):
        try:
            print '%s' % (book.ItemAttributes.Title)
            #print '%s: "%s"' % (book.ItemAttributes.Author,
            #                    book.ItemAttributes.Title)
        except:
            logging.debug("no author or title")

def lookup(asin):
    api = API(locale='jp')
    #item = api.item_lookup(asin, ResponseGroup='OfferFull', Condition='All')
    #item = api.item_lookup(asin)
    item = api.item_lookup(asin, ResponseGroup='Large')
    #logging.debug(etree.tostring(item, pretty_print=True))

    ## title
    logging.debug(item.Items.Item.ItemAttributes.Title)
    ## package_dimensions
    #logging.debug(item.Items.Item.ItemAttributes.PackageDimensions.Height)
    #logging.debug(item.Items.Item.ItemAttributes.PackageDimensions.Width)
    #logging.debug(item.Items.Item.ItemAttributes.PackageDimensions.Height)
    ## Quantity
    #logging.debug(item.Items.Item.ItemAttributes.PackageQuantity)

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    #search()
    #logging.debug(sys.argv[1])
    lookup(sys.argv[1])
