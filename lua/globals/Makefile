MK_CFG_DIR = /opt/local/share/make_cfg
include $(MK_CFG_DIR)/make.defs

EXETARGET = main
CSRC = main.c
CXXSRC = 

WARN +=
OPPFLAGS += -I/opt/local/include
LDFLAGS = -L/opt/local/lib
LDLIBS = -llua

include $(MK_CFG_DIR)/make.rules
