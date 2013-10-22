#include <stdio.h>
#include "zhelpers.h"

int main (void)
{
    void *ctx = zmq_ctx_new();
    void *sub = zmq_socket(ctx, ZMQ_SUB);
    void *dealer = zmq_socket(ctx, ZMQ_DEALER);

    zmq_setsockopt(sub,    ZMQ_SUBSCRIBE, "",   0);
    zmq_setsockopt(dealer, ZMQ_IDENTITY,  "c1", 2);

    zmq_connect(sub,    "tcp://localhost:9998");
    zmq_connect(dealer, "tcp://localhost:9997");

    while (1) {
        fprintf(stderr, "receiving...\n");
        char *cmd = s_recv(sub);
        fprintf(stderr, "cmd: %s\n", cmd);

        s_send(dealer, cmd);
        free (cmd);
    }

    zmq_close(sub);
    zmq_close(dealer);
    zmq_ctx_destroy(ctx);
    return 0;
}
