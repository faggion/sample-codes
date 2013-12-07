# coding: utf-8
import sys, logging, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))+'/../src')

import tanarky.api.server

if __name__ == '__main__':
    logging.basicConfig()
    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
    tanarky.api.server.app.run(debug=True, host='0.0.0.0')
