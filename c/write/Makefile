.PHONY: build test test2 clean tmpclean

build:
	gcc write_load.c  -o wl
	gcc write_load2.c -o wl2

test:
	/usr/bin/time -p ./wl    512 10000
	/usr/bin/time -p ./wl   1024 10000
	/usr/bin/time -p ./wl   2048 10000
	/usr/bin/time -p ./wl   4096 10000
	/usr/bin/time -p ./wl   8192 10000
	/usr/bin/time -p ./wl  16384 10000

test2:
	/usr/bin/time -p ./wl2   512 10000
#	make tmpclean
	/usr/bin/time -p ./wl2  1024 10000
#	make tmpclean
	/usr/bin/time -p ./wl2  2048 10000
#	make tmpclean
	/usr/bin/time -p ./wl2  4096 10000
#	make tmpclean
	/usr/bin/time -p ./wl2  8192 10000
#	make tmpclean
	/usr/bin/time -p ./wl2 16384 10000
#	make tmpclean

tmpclean:
	find tmp/ -type f | xargs -r rm 

clean:
	make tmpclean
	find . -name "*~"  | xargs -r rm
	find . -name "wl*" | xargs -r rm