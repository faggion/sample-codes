# coding: utf-8
import os, logging, unittest, tempfile

#import eventregist.token

class EventRegistTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_true(self):
        assert True

    def test_token(self):
        assert True

        #data = {u"expire": 12345,
        #        "appid": u"あああ",
        #        "scope": "hoge"}
        #enc = eventregist.token.Access.encode(data)
        #logging.debug(enc)
        #logging.debug(eventregist.token.Access.decode(enc))
        #logging.debug(eventregist.token.Access.decode(enc)['appid'])

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    unittest.main()
