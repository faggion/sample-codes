MKCFG_DIR = ../../gnu_make/nmake_cfg
include $(MKCFG_DIR)/make.defs

EXETARGET = main
CSRC = 
CXXSRC = $(EXETARGET).cc

#OPPFLAGS += -I../src -I/opt/local/include
#LDFLAGS = -L/opt/local/lib
#LDLIBS = -llua
OPPFLAGS += -I../src -I/usr/include/lua5.1
LDFLAGS = -L/usr/lib
LDLIBS = -llua5.1

include $(MKCFG_DIR)/make.rules.formac
