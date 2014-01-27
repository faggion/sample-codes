import os
import sys

sys.path.insert(0, 'lib.zip')

app_root_dir = os.path.dirname(__file__)
server_lib_dir = os.path.join(app_root_dir, 'server/lib')
if server_lib_dir not in sys.path:
    sys.path.insert(0, server_lib_dir)
