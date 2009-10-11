.PHONY: all foo bar clean
SUBDIR = foo bar
all: $(SUBDIR)
clean: 
	$(MAKE) TARGET=$@
#	do clean

$(SUBDIR):
	$(MAKE) --directory=$@ $(TARGET)

