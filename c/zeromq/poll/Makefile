MK_CFG_DIR = /home/z/share/make_cfg
include $(MK_CFG_DIR)/make.defs

EXETARGET = server
CSRC = server.c

WARN +=
OPPFLAGS += -I/usr/local/include
LDFLAGS = -L/usr/local/lib
LDLIBS = -lzmq

include $(MK_CFG_DIR)/make.rules
