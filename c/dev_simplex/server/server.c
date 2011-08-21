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

void
server_read(int fd, short event, void *arg)
{
    int receive = -1;
    int len = -1;
    struct event *ev = arg;

    /* Reschedule this event */
    event_add(ev, NULL);

    len = read(fd, (void *)&receive, sizeof(receive));

    if (len == -1) {
        perror("read");
        return;
    } else if (len == 0) {
        fprintf(stderr, "Connection closed\n");
        return;
    }
    fprintf(stdout, "Received %d\n", receive);

    //// Calculate something.
    //receive += 100;
    //
    //len = write (fd, (void *)&receive, sizeof(receive));
    //if (len == -1) {
    //    perror("write");
    //    return;
    //}
    //fprintf(stdout, "Returned %d\n", receive);
}

//int main (int argc, char **argv){
int main (void){
    struct event ev;
    int socket;
    char device[] = "/dev/simplex.0";

    socket = open (device, O_RDWR | O_NONBLOCK, 0);

    if (socket == -1) {
        perror("open");
        exit (1);
    }

    fprintf(stderr, "polling device %s\n", device);
    event_init();
    event_set(&ev, socket, EV_READ, server_read, &ev);
    event_add(&ev, NULL);
    event_dispatch();
    return (0);
}
