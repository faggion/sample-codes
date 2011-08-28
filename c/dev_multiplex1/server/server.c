#include <sys/types.h>
#include <sys/stat.h>
#include <sys/queue.h>
#include <unistd.h>
#include <sys/time.h>
#include <fcntl.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>

#include <event.h>

#include <tcutil.h>

#define NDEV 4

static TCMAP *mymap = NULL;
struct fdmap {
    int fd;
    int minor;
};

void
server_read(int fd, short event, void *arg)
{
    char receive;
    int len = -1;
    int size;
    struct event *ev = arg;
    const struct fdmap *f;

    printf("received0[%d]\n", fd);

    /* Reschedule this event */
    event_add(ev, NULL);

    /* find minor id from fd */
    f = tcmapget(mymap, &fd, sizeof(int), &size);
    if(f != 0){
        printf("null \n");
        len = read(fd, (void *)&receive, 1);
        if (len < 0) {
            perror("read");
            return;
        }
        printf("Received from device[%d]\n", f->minor);
    }
    return;
}

//int main (int argc, char **argv){
int main (void){
    struct event ev;
    struct fdmap fm;
    int sock0,sock2;
    char dev0[] = "/dev/multiplex1.0";
    char dev2[] = "/dev/multiplex1.2";

    mymap = tcmapnew();
    event_init();

    sock0 = open (dev0, O_RDWR | O_NONBLOCK, 0);
    if (sock0 == -1) {
        perror("open sock0");
        exit (1);
    }
    fm.fd    = sock0;
    fm.minor = 0;
    tcmapput(mymap, &sock0, sizeof(int), &fm, sizeof(struct fdmap));
    printf("polling device %s(%d)\n", dev0, sock0);
    event_set(&ev, sock0, EV_READ, server_read, &ev);

    sock2 = open (dev2, O_RDWR | O_NONBLOCK, 0);
    if (sock2 == -1) {
        perror("open sock2");
        exit (1);
    }
    fm.fd    = sock2;
    fm.minor = 2;
    tcmapput(mymap, &sock2, sizeof(int), &fm, sizeof(struct fdmap));
    printf("polling device %s(%d)\n", dev2, sock2);
    event_set(&ev, sock2, EV_READ, server_read, &ev);

    event_add(&ev, NULL);
    event_dispatch();
    return (0);
}
