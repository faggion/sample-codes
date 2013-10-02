MKCFG_DIR = /home/z/share/make_cfg
include $(MKCFG_DIR)/make.defs

LIBNAME = nshmhash
LIBVERSION = 1
CSRC = $(LIBNAME).c
CXXSRC = 

CHDS = $(LIBNAME).h
CXXHDS = 

WARN +=
OPPFLAGS += -I. -I/home/z/include/nshm
LDFLAGS = -L/home/z/lib
LDLIBS = -lnshm

include $(MKCFG_DIR)/make.rules

SO_INSTALL_DIR = /home/z/lib
HD_INSTALL_DIR = /home/z/include/$(LIBNAME)

install: all
	sudo install $(SOTARGET) $(SO_INSTALL_DIR)/
	sudo mkdir -p $(HD_INSTALL_DIR)
	sudo install $(CHDS) $(HD_INSTALL_DIR)/
	sudo ln -sf $(SO_INSTALL_DIR)/$(SOTARGET) $(SO_INSTALL_DIR)/$(LNTARGET)

uninstall:
	sudo rm $(SO_INSTALL_DIR)/$(SOTARGET) $(SO_INSTALL_DIR)/$(LNTARGET)
	sudo rm -rf $(HD_INSTALL_DIR)
