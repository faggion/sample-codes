#include <stdio.h>
#include <stdlib.h>
#include <sys/queue.h>
#include <event.h>
#include <evhttp.h>

#define PORT 8080

void root_handler(struct evhttp_request *req, void *arg)
{
    struct evbuffer *buf = evbuffer_new();
    if (buf) {
        evbuffer_add_printf(buf, "Hello evhttp World!");
        evhttp_send_reply(req, HTTP_OK, "OK", buf);
    }else{
        fprintf(stderr, "failed to create response buffer¥n");
    }
}


int main (int argc, char *argv[])
{
    struct evhttp *httpd;

    event_init();
    httpd = evhttp_start ("0.0.0.0", PORT);

    if(httpd){
        evhttp_set_cb (httpd, "/", root_handler, NULL);
        event_dispatch();
        evhttp_free (httpd);

        return 0;
    }
    fprintf(stderr, "bind failed¥n");
    return 1;
}
