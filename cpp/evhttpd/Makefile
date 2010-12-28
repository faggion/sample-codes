.PHONEY: clean binary

#gcc -I/usr/include/ -levent evhttpd.c

HTTPD   = evhttpd
LDFLAGS = -levent
CFLAGS  = -g -Wall

$(HTTPD): $%

binary:
	gcc -c evhttpd.c
	gcc -lrt -o $(HTTPD) evhttpd.o /usr/lib/libevent.a /usr/lib/libevent_extra.a /usr/lib/libevent_core.a

clean:
	$(RM) *.o $(HTTPD)