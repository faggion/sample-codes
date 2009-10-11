.PHONY: all install

INSTALL_DIR = /var/www/nginx-default

all: install

install:
	rsync -av -e ssh js  $(INSTALL_DIR)/
	rsync -av -e ssh css $(INSTALL_DIR)/
	cp cat_calendar.html $(INSTALL_DIR)