#include <stdio.h>
#include <string.h>

#include <zmq.h>

int main (void)
{
    int rc;
    size_t size;
    char *buf = NULL;

    void *ctx = zmq_ctx_new();
    void *sub = zmq_socket(ctx, ZMQ_SUB);
    void *dealer = zmq_socket(ctx, ZMQ_DEALER);

    zmq_setsockopt(sub,    ZMQ_SUBSCRIBE, "",   0);
    zmq_setsockopt(dealer, ZMQ_IDENTITY,  "c1", 2);

    zmq_connect(sub,    "tcp://localhost:9998");
    zmq_connect(dealer, "tcp://localhost:9997");

    while (1) {
        fprintf(stderr, "receiving...\n");

        zmq_msg_t msg;
        rc = zmq_msg_init(&msg);
        rc = zmq_msg_recv (&msg, sub, 0);
        fprintf(stderr, "msg size: %ld\n", zmq_msg_size(&msg));

        size = zmq_msg_size(&msg) + 1;
        buf = (char *)malloc(size);
        memset(buf, 0, size);
        memcpy(buf, zmq_msg_data(&msg), size - 1);
        fprintf(stderr, "msg data: %s\n", buf);

        zmq_msg_close(&msg);
    }

    zmq_close(sub);
    zmq_close(dealer);
    zmq_ctx_destroy(ctx);
    return 0;
}
