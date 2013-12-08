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
        datas = [
            {'id': 1, 'width': 300, 'height': 250},
            {'id': 2, 'width': 320, 'height':  50},
            ]
        url = '/cpaopt/adsize'
        for data in datas:
            rv = self.app.post(url, headers=headers, data=json.dumps(data))
            #logging.debug(rv.data)
            rv = self.app.get('%s/%d' % (url, data['id']))

        rv = self.app.get('%s/%d' % (url, 99))

    def test_02_media(self):
        pass

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    unittest.main()
