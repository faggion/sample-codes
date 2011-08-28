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

#include <tcutil.h>

struct fdinfo {
    int fd;
    int dev;
    int is_remote;
    int group;
};

int main (void){
    TCMAP *mymap = tcmapnew();
    //struct fdinfo fdi, *f;
    struct fdinfo fdi;
    const struct fdinfo *f;
    int a,b,c,d,e;
    const int *ret;
    a = 10;
    b = 100;

    tcmapput(mymap, &a, sizeof(int), &b, sizeof(int));
    ret = tcmapget(mymap, &a, sizeof(int), &c);
    printf("ret=%d sp=%d\n", *ret, c);

    d = 7;
    fdi.fd  = 3;
    fdi.dev = 2;
    fdi.is_remote = false;
    fdi.group = 103;
    tcmapput(mymap, &d, sizeof(int), &fdi, sizeof(struct fdinfo));
    f = tcmapget(mymap, &d, sizeof(int), &e);
    printf("fdinfo->group=%d size=%d\n", f->group, e);

    tcmapdel(mymap);
    return 0;
}
