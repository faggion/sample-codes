MK_CFG_DIR = /home/z/share/make_cfg
include $(MK_CFG_DIR)/make.defs

#LIBNAME = nshm
#LIBVERSION=1
CSRC = sample.c
EXETARGET = sample

WARN +=
OPPFLAGS += -I/home/z/include/nshm
DEPOBJS =
LDFLAGS = -L/home/z/lib 
LDLIBS  = -lpthread -lnshm

include $(MK_CFG_DIR)/make.rules
