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

int main (int argc, char **argv){
    int request = -999;
    int response = -999;
    int len = -1;
    int socket;
    char device[] = "/dev/simplex.1";

    if(argc < 2){
        fprintf(stderr, "invalid argc %d\n", argc);
        return -1;
    }
    request = atoi(argv[1]);

    socket = open(device, O_RDWR | O_NONBLOCK, 0);

    if (socket == -1) {
        perror("open");
        exit (1);
    }

    len = write (socket, (void *)&request, sizeof(request));
    if (len == -1) {
        perror("write");
        return -1;
    }

    //len = read(socket, (void *)&response, sizeof(response));
    //if (len == -1) {
    //    perror("read");
    //    return -1;
    //}
    //fprintf(stdout, "received response %d\n", response);

    return 0;
}
