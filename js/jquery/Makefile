.PHONY: all install

#INSTALL_DIR = /var/www/nginx-default/tanarky/jquery
INSTALL_DIR = /usr/share/tanarky/htdocs/tmp/jquery

all: install

install:
	rsync -av -e ssh --delete --exclude .git htdocs/  $(INSTALL_DIR)/

# perl upload_all.pl --host=ftp.geocities.jp --user=tanarky --pass='' --dir='./jquery'