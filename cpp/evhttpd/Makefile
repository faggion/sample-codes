.PHONEY: clean

#gcc -I/usr/include/ -levent evhttpd.c

HTTPD   = evhttpd
LDFLAGS = -levent
CFLAGS  = -g -Wall

$(HTTPD): $%

clean:
	$(RM) *.o $(HTTPD)