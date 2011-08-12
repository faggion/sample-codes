ifndef LINUX_HEADERS
LINUX_HEADERS:=$(shell if [ -e /usr/src/linux-headers-`uname -r` ] ;	then echo /usr/src/linux-headers-`uname -r` ; else echo /usr/src/linux-`uname -r` ; fi)
endif

TARGET:= lock.ko

all: ${TARGET}

lock.ko: lock.c
	make -C ${LINUX_HEADERS} M=`pwd` V=1 modules

clean:
	make -C ${LINUX_HEADERS} M=`pwd` V=1 clean

install: all
	sudo mknod /dev/lock.1 c 0x0721 1
	sudo mknod /dev/lock.2 c 0x0721 2
	sudo chmod 0666 /dev/lock.1
	sudo chmod 0666 /dev/lock.2
	sudo insmod lock.ko

uninstall:
	sudo rmmod lock
	sudo rm -f /dev/lock.1
	sudo rm -f /dev/lock.2

obj-m:= lock.o

clean-files := *.o *.ko *.mod.[co] *~

