.PHONY: all

all: 
	python bootstrap.py --distribute && bin/buildout

clean:
	rm -rf bin/ develop-eggs/ eggs/ parts/ *.egg-info/
	find . -name "*.pyc" -or -name "*~" | perl -nle unlink

update_buildout:
	wget "http://svn.zope.org/*checkout*/zc.buildout/trunk/bootstrap/bootstrap.py"

