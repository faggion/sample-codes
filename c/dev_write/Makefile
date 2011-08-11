ifndef LINUX_HEADERS
LINUX_HEADERS:=$(shell if [ -e /usr/src/linux-headers-`uname -r` ] ;	then echo /usr/src/linux-headers-`uname -r` ; else echo /usr/src/linux-`uname -r` ; fi)
endif

TARGET:= write.ko

all: ${TARGET}

write.ko: write.c
	make -C ${LINUX_HEADERS} M=`pwd` V=1 modules

clean:
	make -C ${LINUX_HEADERS} M=`pwd` V=1 clean

install: all
	sudo mknod /dev/write.1 c 0x0721 1
	sudo mknod /dev/write.2 c 0x0721 2
	sudo chmod 0666 /dev/write.1
	sudo chmod 0666 /dev/write.2
	sudo insmod write.ko

uninstall:
	sudo rmmod write
	sudo rm -f /dev/write.1
	sudo rm -f /dev/write.2

obj-m:= write.o

clean-files := *.o *.ko *.mod.[co] *~

