.PHONY: install clean etc pkg

SUBDIR = etc pkg

install: $(SUBDIR)

clean:
	$(MAKE) TARGET=$@

$(SUBDIR):
	$(MAKE) --directory=$@ $(TARGET)
