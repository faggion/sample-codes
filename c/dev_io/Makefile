ifndef LINUX_HEADERS
LINUX_HEADERS:=$(shell if [ -e /usr/src/linux-headers-`uname -r` ] ;	then echo /usr/src/linux-headers-`uname -r` ; else echo /usr/src/linux-`uname -r` ; fi)
endif

MAJOR=280

TARGET:= io.ko

all: ${TARGET}

io.ko: io.c
	make -C ${LINUX_HEADERS} M=`pwd` V=1 modules

clean:
	make -C ${LINUX_HEADERS} M=`pwd` V=1 clean

install: all
	sudo insmod io.ko
	sudo mknod /dev/io.1 c $(MAJOR) 1
	sudo mknod /dev/io.2 c $(MAJOR) 2
	sudo chmod 0666 /dev/io.1
	sudo chmod 0666 /dev/io.2

uninstall:
	sudo rm -f /dev/io.1
	sudo rm -f /dev/io.2
	sudo rmmod io

obj-m:= io.o

clean-files := *.o *.ko *.mod.[co] *~

