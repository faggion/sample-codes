#include <stdio.h>
#include <zmq.h>

#include "zhelpers.h"

int main (void)
{
    int rc;
    void *ctx = zmq_ctx_new();
    void *sock1 = zmq_socket(ctx, ZMQ_REP);
    void *sock2 = zmq_socket(ctx, ZMQ_REP);
    void *sock3 = zmq_socket(ctx, ZMQ_REP);
    zmp_bind(sock1, 'tcp://*:9999');
    zmp_bind(sock2, 'tcp://*:9998');
    zmp_bind(sock3, 'tcp://*:9997');

    zmq_pollitem_t items[] = {
        { sock1, 0, ZMQ_POLLIN, 0 },
        { sock2, 0, ZMQ_POLLIN, 0 },
        { sock3, 0, ZMQ_POLLIN, 0 },
    };

    while(1){
        zmq_msg_t msg;
        char *buf  = NULL;
        void *sock = NULL;
        size_t size;

        fprintf(stderr, "polling ...\n");
        rc = zmq_poll(items, 1, 1000 * ZMQ_POLL_MSEC);
        if(rc == -1) return NULL; // Interrupted

        int i = -1;
        if(items[0].revents & ZMQ_POLLIN){
            rc = zmq_msg_init(&msg);
            sock = sock1;
            rc = zmq_msg_recv(&msg, sock, 0);
            size = zmq_msg_size(&msg) + (size_t)1;
            buf = (char *)malloc(size);
            memset(buf, 0, size);
            memcpy(buf, zmq_msg_data(&msg), size - (size_t)1);
            fprintf(stderr, "msg => %s\n", buf);
            free(buf); buf = NULL;
            zmq_msg_close (&msg);
        }
        if(items[1].revents & ZMQ_POLLIN){
            rc = zmq_msg_init(&msg);
            sock = sock2;
            rc = zmq_msg_recv(&msg, sock, 0);
            size = zmq_msg_size(&msg) + (size_t)1;
            buf = (char *)malloc(size);
            memset(buf, 0, size);
            memcpy(buf, zmq_msg_data(&msg), size - (size_t)1);
            fprintf(stderr, "msg => %s\n", buf);
            free(buf); buf = NULL;
            zmq_msg_close (&msg);
        }
        if(items[2].revents & ZMQ_POLLIN){
            rc = zmq_msg_init(&msg);
            sock = sock3;
            rc = zmq_msg_recv(&msg, sock, 0);
            size = zmq_msg_size(&msg) + (size_t)1;
            buf = (char *)malloc(size);
            memset(buf, 0, size);
            memcpy(buf, zmq_msg_data(&msg), size - (size_t)1);
            fprintf(stderr, "msg => %s\n", buf);
            free(buf); buf = NULL;
            zmq_msg_close (&msg);
        }
    }

    zmq_close(sock1);
    zmq_close(sock2);
    zmq_close(sock3);
    zmq_ctx_destroy(ctx);
    return 0;
}
