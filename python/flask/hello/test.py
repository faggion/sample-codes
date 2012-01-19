import os
import hello
import unittest
import tempfile
import logging

class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        self.app = hello.app.test_client()

    def tearDown(self):
        pass

    def mytest(self):
        ret = self.app.get('/')
        assert u'hello' in ret.data

if __name__ == '__main__':
    unittest.main()
