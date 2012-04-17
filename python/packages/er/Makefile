.PHONY: install

clean:
	rm -rf dist build *.egg-info

install: clean uninstall
	python setup.py test
	python setup.py sdist
	pip install dist/*tar.gz

uninstall:
	rm -rf ~/.virtualenvs/2.7.2/lib/python2.7/site-packages/eventregist*
