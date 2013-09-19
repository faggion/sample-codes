MKCFGDIR = ../../../gnu_make/nmake_cfg
include $(MKCFGDIR)/make.defs

LIBNAME = sptree
LIBVERSION = 1
CSRC = sptree.c
CXXSRC = 

include $(MKCFGDIR)/make.rules

INSTALLDIR = /home/z/lib

install:
	sudo install $(SOTARGET) $(INSTALLDIR)/
	sudo ln -sf $(INSTALLDIR)/$(SOTARGET) $(INSTALLDIR)/$(LNTARGET)