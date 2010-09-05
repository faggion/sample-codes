.PHONY: build test test2 test3 clean tmpclean

build:
#	gcc write_load.c  -o wl
#	gcc write_load2.c -o wl2
#	gcc alloc.c       -o al
	gcc rand_write.c  -o ra

test:
	/usr/bin/time -p ./wl    512 10000
	/usr/bin/time -p ./wl   1024 10000
	/usr/bin/time -p ./wl   2048 10000
	/usr/bin/time -p ./wl   4096 10000
	/usr/bin/time -p ./wl   8192 10000
	/usr/bin/time -p ./wl  16384 10000

test3:
	echo "512byte ->"
	/usr/bin/time -p ./ra  1  1024
	echo "1k byte ->"
	/usr/bin/time -p ./ra  2  1024
	echo "2k byte ->"
	/usr/bin/time -p ./ra  4  1024
	echo "4k byte ->"
	/usr/bin/time -p ./ra  8  1024
	echo "8k byte ->"
	/usr/bin/time -p ./ra  16 1024
	echo "16k byte ->"
	/usr/bin/time -p ./ra  32 1024
	echo "32k byte ->"
	/usr/bin/time -p ./ra  64 1024
	echo "64k byte ->"
	/usr/bin/time -p ./ra  128 1024
	echo "128k byte ->"
	/usr/bin/time -p ./ra  256 1024

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
	rm a.out initfile al ra rand bigfile file
