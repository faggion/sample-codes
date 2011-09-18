#!/usr/bin/python
# -*- coding: utf-8 -*-
import ConfigParser, os

config = ConfigParser.ConfigParser()
#config.read("config")
config.read(".config")

print config.get("section", "foo")
print config.get("section", "baz")
