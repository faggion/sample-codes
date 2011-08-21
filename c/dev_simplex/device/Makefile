ifndef LINUX_HEADERS
LINUX_HEADERS:=$(shell if [ -e /usr/src/linux-headers-`uname -r` ] ;	then echo /usr/src/linux-headers-`uname -r` ; else echo /usr/src/linux-`uname -r` ; fi)
endif

TARGET:= simplex.ko

all: ${TARGET}

simplex.ko: simplex.c
	make -C ${LINUX_HEADERS} M=`pwd` V=1 modules

clean:
	make -C ${LINUX_HEADERS} M=`pwd` V=1 clean

install: all
	sudo mknod /dev/simplex.0 c 280 0
	sudo mknod /dev/simplex.1 c 280 1
	sudo chmod 0666 /dev/simplex.0
	sudo chmod 0666 /dev/simplex.1
	sudo insmod simplex.ko

uninstall:
	sudo rmmod simplex
	sudo rm -f /dev/simplex.0
	sudo rm -f /dev/simplex.1

obj-m:= simplex.o

clean-files := *.o *.ko *.mod.[co] *~

