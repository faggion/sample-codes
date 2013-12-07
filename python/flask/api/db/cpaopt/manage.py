#!/usr/bin/env python
from migrate.versioning.shell import main

if __name__ == '__main__':
    main(url='sqlite:////tmp/cpaopt.sqlite', debug='False', repository='.')
