# coding: utf-8
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))+'/../src')

import unittest, logging, traceback, json
import tanarky.api.server
from tanarky.api.models import Base
from tanarky.api.helpers import engine

headers = {
    'Content-type': 'application/json; charset=utf-8'
}
class CpaOptimizerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = tanarky.api.server.app.test_client()

    def tearDown(self):
        pass

    def test_00_cleanup(self):
        for tbl in reversed(Base.metadata.sorted_tables):
            engine.execute(tbl.delete())

    def test_01_adsize(self):
        data = {'foo':123}
        rv = self.app.post('/cpaopt/adsize', headers=headers, data=json.dumps(data))

    def test_02_media(self):
        pass

if __name__ == '__main__':
    unittest.main()
