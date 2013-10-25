#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <errno.h>
#include <stdint.h>
#include <fcntl.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <time.h>
#include <stdio.h>
#include <libgen.h>

#include <zmq.h>

void dump(void *sock, const char *name){
    const char ok[] = "OK";
    char *buf  = NULL;
    size_t size;
    zmq_msg_t msg;
    int rc = zmq_msg_init(&msg);

    rc = zmq_msg_recv(&msg, sock, 0);
    size = zmq_msg_size(&msg) + (size_t)1;
    buf = (char *)malloc(size);
    memset(buf, 0, size);
    memcpy(buf, zmq_msg_data(&msg), size - (size_t)1);
    fprintf(stderr, "from %s => %s\n", name, buf);
    free(buf); buf = NULL;

    rc = zmq_send(sock, ok, strlen(ok), 0);
    fprintf(stderr, "sent bytes %d\n", rc);

    zmq_msg_close(&msg);
}

int main (void)
{
    int rc;
    void *ctx = zmq_ctx_new();
    void *sock1 = zmq_socket(ctx, ZMQ_REP);
    //void *sock2 = zmq_socket(ctx, ZMQ_REP);
    //void *sock3 = zmq_socket(ctx, ZMQ_REP);

    if(sock1 == NULL){
        fprintf(stderr, "sock1 null");
        return -1;
    }
    //if(sock2 == NULL){
    //    fprintf(stderr, "sock2 null");
    //    return -1;
    //}
    //if(sock3 == NULL){
    //    fprintf(stderr, "sock3 null");
    //    return -1;
    //}

    //zmq_bind(sock1, "tcp://localhost:9999");
    zmq_bind(sock1, "tcp://127.0.0.1:9999");
    //zmq_bind(sock1, "tcp://*:9999");
    //zmq_bind(sock2, "tcp://localhost:9998");
    //zmq_bind(sock3, "tcp://localhost:9997");

    zmq_pollitem_t items[] = {
        { sock1, 0, ZMQ_POLLIN, 0 },
        //{ sock2, 0, ZMQ_POLLIN, 0 },
        //{ sock3, 0, ZMQ_POLLIN, 0 },
    };

    while(1){
        fprintf(stderr, "polling ...\n");
        rc = zmq_poll(items, 1, 3000);
        fprintf(stderr, "finished polling.\n");

        if(rc == -1) break; // Interrupted

        fprintf(stderr, "rc = %d\n", rc);
        //fprintf(stderr, "revents = %d\n", items[0].revents);

        if(items[0].revents & ZMQ_POLLIN){
            fprintf(stderr, "sock1\n");
            dump(sock1, "sock1");
        }
        //if(items[1].revents & ZMQ_POLLIN){
        //    fprintf(stderr, "sock2\n");
        //    dump(sock2, "sock2");
        //}
        //if(items[2].revents & ZMQ_POLLIN){
        //    fprintf(stderr, "sock3\n");
        //    dump(sock3, "sock3");
        //}
    }

    zmq_close(sock1);
    //zmq_close(sock2);
    //zmq_close(sock3);
    zmq_ctx_destroy(ctx);
    return 0;
}
