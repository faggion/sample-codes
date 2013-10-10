.PHONY: all clean lib test

SUBDIR = lib test

all: $(SUBDIR)

clean:
	$(MAKE) TARGET=$@

$(SUBDIR):
	$(MAKE) --directory=$@ $(TARGET)