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

void dump(void *cmd, void *out, const char *name){
    //const char ok[] = "OK";
    char *buf  = NULL;
    size_t size;
    zmq_msg_t msg;
    int rc = zmq_msg_init(&msg);

    /* メッセージ受信 */
    rc = zmq_msg_recv(&msg, cmd, 0);
    size = zmq_msg_size(&msg) + (size_t)1;
    buf = (char *)malloc(size);
    memset(buf, 0, size);
    memcpy(buf, zmq_msg_data(&msg), size - (size_t)1);
    fprintf(stderr, "from %s => %s\n", name, buf);
    free(buf); buf = NULL;

    /* メッセージ送信 */
    //rc = zmq_send(cmd, ok, strlen(ok), 0);

    rc = zmq_msg_send(&msg, out, 0);
    fprintf(stderr, "sent bytes %d\n", rc);

    zmq_msg_close(&msg);
}

int main(const int argc, const char **argv){
    int rc;

    if(argc < 3){
        fprintf(stderr, "Usage: ./dealer [NAME] [CMDPORT]\n");
        return -1;
    }

    void *ctx = zmq_ctx_new();
    void *sock1 = zmq_socket(ctx, ZMQ_REP);
    void *sock2 = zmq_socket(ctx, ZMQ_DEALER);

    if(sock1 == NULL){
        fprintf(stderr, "sock1 null");
        return -1;
    }
    if(sock2 == NULL){
        fprintf(stderr, "sock2 null");
        return -1;
    }

    zmq_bind(sock1, argv[2]);
    zmq_setsockopt(sock2, ZMQ_IDENTITY, argv[1], strlen(argv[1]));
    zmq_connect(sock2, "tcp://127.0.0.1:5555");

    zmq_pollitem_t items[] = {
        { sock1, 0, ZMQ_POLLIN, 0 },
    };
    long itemcount = sizeof(items)/sizeof(zmq_pollitem_t);
    fprintf(stderr, "zmq_pollitem_t size %ld\n", itemcount);

    while(1){
        fprintf(stderr, "polling ...\n");
        rc = zmq_poll(items, (int)itemcount, 3000);
        fprintf(stderr, "finished polling.\n");

        if(rc == -1) break; // Interrupted

        fprintf(stderr, "rc = %d\n", rc);

        if(items[0].revents & ZMQ_POLLIN){
            fprintf(stderr, "sock1\n");
            dump(sock1, sock2, argv[1]);
        }
    }

    zmq_close(sock1);
    zmq_close(sock2);
    zmq_ctx_destroy(ctx);
    return 0;
}
