.PHONY: install clean 

PYENV     = /usr/share/erapi2
NAMESPACE = tanarky
NAME      = examples
VENVROOT  = $(PYENV)
VENVBIN   = $(VENVROOT)/bin
PYVER     = 2.6
PYTHON    = $(VENVBIN)/python
PIP       = $(VENVBIN)/pip

install: clean uninstall
	$(PYTHON) setup.py test
	$(PYTHON) setup.py sdist
	$(PIP) install dist/*tar.gz

clean: 
	rm -rf dist build src/*.egg-info

freeze: uninstall
	$(PIP) freeze | tee requirements.txt

uninstall:
	rm -rf $(VENVROOT)/lib/python$(PYVER)/site-packages/$(NAMESPACE)/$(NAME)*
	rm -rf $(VENVROOT)/lib/python$(PYVER)/site-packages/$(NAMESPACE).$(NAME)*
