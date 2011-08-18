ifndef LINUX_HEADERS
LINUX_HEADERS:=$(shell if [ -e /usr/src/linux-headers-`uname -r` ] ;	then echo /usr/src/linux-headers-`uname -r` ; else echo /usr/src/linux-`uname -r` ; fi)
endif

TARGET:= poll.ko

all: ${TARGET}

poll.ko: poll.c
	make -C ${LINUX_HEADERS} M=`pwd` V=1 modules

clean:
	make -C ${LINUX_HEADERS} M=`pwd` V=1 clean

install: all
	sudo mknod /dev/poll.1 c 280 1
	sudo mknod /dev/poll.2 c 280 2
	sudo chmod 0666 /dev/poll.1
	sudo chmod 0666 /dev/poll.2
	sudo insmod poll.ko

uninstall:
	sudo rmmod poll
	sudo rm -f /dev/poll.1
	sudo rm -f /dev/poll.2

obj-m:= poll.o

clean-files := *.o *.ko *.mod.[co] *~

