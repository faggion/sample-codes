# coding: utf-8
import logging, os, sys, traceback

class Foo(object):
    def create(self):
        logging.debug('called create()')

    def close(self):
        logging.debug('called close()')

    def __iter__(self):
        logging.debug('called __iter__()')

    def __enter__(self):
        logging.debug('called __enter__()')
        self.create()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    logging.debug('calling constructor')
    ff = Foo()
    logging.debug('finished calling constructor')

    logging.debug('calling "with"')
    with Foo() as f:
        logging.debug('inside "with"')
