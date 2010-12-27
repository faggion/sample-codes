.PHONEY: clean

#g++ -I/usr/include/ -levent mt_evhttpd.cpp

HTTPD    = mt_evhttpd
LDFLAGS  = -levent
CPPFLAGS = -g -Wall

$(HTTPD): $%

clean:
	$(RM) *.o $(HTTPD)