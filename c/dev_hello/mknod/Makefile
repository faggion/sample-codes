MK_CFG_DIR = /usr/local/share/make_cfg
include $(MK_CFG_DIR)/make.defs

CSRC = mknod.c
EXETARGET = mknod

WARN +=
OPPFLAGS +=
DEPOBJS =
LDFLAGS =
LDLIBS = 

install: all
	sudo ./mknod

uninstall:
	sudo rm /dev/hello_dev.1

include $(MK_CFG_DIR)/make.rules