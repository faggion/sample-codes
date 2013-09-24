.PHONY: all clean dump dump_header gen replace

SUBDIR = dump dump_header gen replace

all: $(SUBDIR)

clean:
	$(MAKE) TARGET=$@

$(SUBDIR):
	$(MAKE) --directory=$@ $(TARGET)