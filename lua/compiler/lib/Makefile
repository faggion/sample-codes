MKCFG_DIR = ../../../gnu_make/nmake_cfg
include $(MKCFG_DIR)/make.defs

LIBNAME = lua51compiler
LIBVERSION = 1
CSRC = $(LIBNAME).c
CXXSRC = 

CHDS = $(LIBNAME).h
CXXHDS = 

WARN +=
OPPFLAGS += -I../src -I/usr/include/lua5.1
LDFLAGS = -L/usr/lib
LDLIBS = -llua5.1

include $(MKCFG_DIR)/make.rules

SO_INSTALL_DIR = /usr/lib
HD_INSTALL_DIR = /usr/include/$(LIBNAME)

install: all
	sudo install $(SOTARGET) $(SO_INSTALL_DIR)/
	sudo mkdir -p $(HD_INSTALL_DIR)
	sudo install $(CHDS) $(HD_INSTALL_DIR)/
	sudo ln -sf $(SO_INSTALL_DIR)/$(SOTARGET) $(SO_INSTALL_DIR)/$(LNTARGET)

uninstall:
	sudo rm $(SO_INSTALL_DIR)/$(SOTARGET) $(SO_INSTALL_DIR)/$(LNTARGET)
	sudo rm -rf $(HD_INSTALL_DIR)
