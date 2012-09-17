MK_CFG_DIR = /home/z/share/make_cfg
include $(MK_CFG_DIR)/make.defs

EXETARGET = sample1
CSRC = sample1.c
CXXSRC = 

WARN +=
OPPFLAGS +=
LDFLAGS =
LDLIBS = -ljson

include $(MK_CFG_DIR)/make.rules

test:
	valgrind --error-limit=no --leak-check=yes ./sample1 -f config.json

testv:
	valgrind -v --error-limit=no --leak-check=yes ./sample1 -f config.json