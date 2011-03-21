#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docutils.core import publish_parts

input = open('foo.rst').read()
parts = publish_parts(source=input, writer_name='html4css1')
#parts = publish_parts(source=input, writer_name='html4css1',
#                      settings_overrides={'initial_header_level':2})
#parts = publish_parts(source=input, writer_name='s5_html')
print parts['html_body']

#foo="a\naa"
#foo='a\naa'
#print "%s" % foo
#print foo

#print "aaa"
#parts = publish_parts(source='aaa', writer_name='html4css1')
#parts = publish_parts(source='aaa', writer_name='html')
#print parts['html_body']
#print parts['fragment']
