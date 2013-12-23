.PHONY: install clean activate uninstall config_overwrite freeze

PYENV     = $(HOME)/python/2.7.3
NAMESPACE = tanarky
NAME      = util
VENVROOT  = $(PYENV)
VENVBIN   = $(VENVROOT)/bin
PYVER     = 2.7
PYTHON    = $(VENVBIN)/python
PIP       = $(VENVBIN)/pip
SETCONF   = $(VENVBIN)/tanarky_config

install: activate clean uninstall
	$(PYTHON) setup.py test
	$(PYTHON) setup.py sdist
	$(PIP) install dist/*tar.gz

config_overwrite:
	sudo $(SETCONF) --name=$(NAME) --mode=overwrite

config_clear:
	sudo $(SETCONF) --name=$(NAME) --mode=clear

clean: 
	rm -rf dist build src/*.egg-info

activate:
	$(PIP) install -r requirements.txt

freeze: uninstall
	$(PIP) freeze | tee requirements.txt

uninstall:
	rm -rf $(VENVROOT)/lib/python$(PYVER)/site-packages/$(NAMESPACE)/$(NAME)*
	rm -rf $(VENVROOT)/lib/python$(PYVER)/site-packages/$(NAMESPACE).$(NAME)*
