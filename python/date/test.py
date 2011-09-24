# -*- coding: utf-8 -*-

import email.utils, time

print email.utils.formatdate(time.time() - 86400, localtime=False, usegmt=True)
