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
#define BUFSIZ 32

TCMAP *devmap = NULL;
struct device {
    int fd;
    int minor;
    struct event ev;
} devices[NDEV/2];

void
server_read(int fd, short event, void *arg)
{
    char receive;
    int len=-1,size;
    const int *i;
    struct event *ev = arg;
    struct device d;

    printf("received0[%d]\n", fd);

    /* Reschedule this event */
    event_add(ev, NULL);

    /* find minor id from fd */
    i = tcmapget(devmap, &fd, sizeof(int), &size);
    if(i != 0){
        d = devices[*i];
        len = read(fd, (void *)&receive, 1);
        if (len < 0) {
            perror("read");
            return;
        }
        printf("Received from device[%d]\n", d.minor);
    }
    return;
}

int main (void)
{
    char buf[BUFSIZ];
    int i;

    devmap = tcmapnew();
    event_init();

    for(i=0;i<NDEV/2;i++){
        snprintf(buf, sizeof(buf), "/dev/multiplex1.%d", i*2);
        devices[i].fd = open (buf, O_RDWR | O_NONBLOCK, 0);
        if(devices[i].fd == -1){
            perror("open sock2");
            exit (1);
        }
        devices[i].minor = i*2;
        tcmapput(devmap, &devices[i].fd, sizeof(int), &i, sizeof(int));
        printf("polling device %s(%d)\n", buf, devices[i].fd);
        event_set(&devices[i].ev, devices[i].fd, EV_READ, server_read, &devices[i].ev);
        event_add(&devices[i].ev, NULL);
    }
    event_dispatch();
    tcmapdel(devmap);
    return (0);
}
