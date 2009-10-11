.PHONY: all clean foo bar baz

SUBDIR = baz foo bar

all: $(SUBDIR)
clean:
	$(MAKE) TARGET=$@

$(SUBDIR):
	$(MAKE) --directory=$@ $(TARGET)
