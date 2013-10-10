MKCFG_DIR = ../../../gnu_make/nmake_cfg
include $(MKCFG_DIR)/make.defs

EXETARGET = main
CSRC = 
CXXSRC = $(EXETARGET).cc

OPPFLAGS += -I../lib -I/usr/include/lua5.1 -I/usr/include/lua51compiler
LDFLAGS = -L/usr/lib
LDLIBS = -llua5.1 -llua51compiler

include $(MKCFG_DIR)/make.rules
