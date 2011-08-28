ifndef LINUX_HEADERS
LINUX_HEADERS:=$(shell if [ -e /usr/src/linux-headers-`uname -r` ] ;	then echo /usr/src/linux-headers-`uname -r` ; else echo /usr/src/linux-`uname -r` ; fi)
endif

TARGET:= multiplex1.ko

all: ${TARGET}

multiplex1.ko: multiplex1.c
	make -C ${LINUX_HEADERS} M=`pwd` V=1 modules

clean:
	make -C ${LINUX_HEADERS} M=`pwd` V=1 clean

install: all
	sudo mknod /dev/multiplex1.0 c 280 0
	sudo mknod /dev/multiplex1.1 c 280 1
	sudo mknod /dev/multiplex1.2 c 280 2
	sudo mknod /dev/multiplex1.3 c 280 3
	sudo chmod 0666 /dev/multiplex1.0
	sudo chmod 0666 /dev/multiplex1.1
	sudo chmod 0666 /dev/multiplex1.2
	sudo chmod 0666 /dev/multiplex1.3
	sudo insmod multiplex1.ko

uninstall:
	sudo rmmod multiplex1
	sudo rm -f /dev/multiplex1.0
	sudo rm -f /dev/multiplex1.1
	sudo rm -f /dev/multiplex1.2
	sudo rm -f /dev/multiplex1.3

obj-m:= multiplex1.o

clean-files := *.o *.ko *.mod.[co] *~

