.PHONY: install

HEADER = HEADER.html
FOOTER = FOOTER.html
INDEX  = build/index.html
CAAT   = /home/satoshi-tanaka/git/CAAT/build

install:
	rm -rf build
	mkdir ./build
	cp -r img build/
	echo '<!DOCTYPE html>' > $(INDEX)
	echo '<head><meta charset="utf8">' >> $(INDEX)
	echo '<meta name="viewport" content="width=device-width; initial-scale=1.0; user-scalable=1;">' >> $(INDEX)
	echo '</head><body style="margin:0;padding:0">' >> $(INDEX)
	echo '<ul>'  >> $(INDEX)
	@LIST=`ls tut*.js`;for x in $$LIST;do cat $(HEADER) $$x $(FOOTER) > build/$$x.html; echo '<li><a href="'$$x'.html">'$$x.html'</a></li>' >> $(INDEX); done;
	echo '</ul></body></html>' >> $(INDEX)
	ln -s $(CAAT) build/lib
	rsync -av -e ssh --delete build/ /var/www/caat/