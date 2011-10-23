import logging, sys

logging.basicConfig(format="%(filename)s:%(lineno)d:%(funcName)s:%(message)s",
                    level=logging.DEBUG)

class Foo(object):
    bar=123

    def __init__(self):
        logging.error("init ok")

    def test(self):
        logging.error("test ok")
        return self.bar * 10

    @classmethod
    def hoge(self):
        logging.error("class method hoge")

def testFunc():
    logging.error("entering")
    logging.error("entering")

testFunc()

logging.error("hoge")
logging.error("hoge")

logging.error(Foo().test())
logging.error(Foo.hoge())
