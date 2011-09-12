ifndef LINUX_HEADERS
LINUX_HEADERS:=$(shell if [ -e /usr/src/linux-headers-`uname -r` ] ;	then echo /usr/src/linux-headers-`uname -r` ; else echo /usr/src/linux-`uname -r` ; fi)
endif

TARGET:= hello.ko

all: ${TARGET}

hello.ko: hello.c
	make -C ${LINUX_HEADERS} M=`pwd` V=1 modules

clean:
	make -C ${LINUX_HEADERS} M=`pwd` V=1 clean

install: all
	sudo insmod hello.ko

uninstall:
	sudo rmmod hello

obj-m:= hello.o

clean-files := *.o *.ko *.mod.[co] *~

