MK_CFG_DIR = /home/z/share/make_cfg
include $(MK_CFG_DIR)/make.defs

EXETARGET = dumper
CSRC = 
CXXSRC = dumper.cc

WARN +=
OPPFLAGS += -I../lib -I/home/z/include/nshm -I/home/z/include/nshmhash
LDFLAGS = -L/home/z/lib
LDLIBS = -lnshm -lnshmhash

include $(MK_CFG_DIR)/make.rules
