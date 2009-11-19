.PHONY: all install

INSTALL_DIR = /var/www/nginx-default/tanarky/yui

all: install

install:
	rsync -av -e ssh --delete --exclude .git htdocs/  $(INSTALL_DIR)/
