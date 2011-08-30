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
    {
        TCMAP *mymap = tcmapnew();
        struct fdinfo fdi;
        int a=10,b=100,c,d=7,e;
        const struct fdinfo *f;
        const int *ret;

        tcmapput(mymap, &a, sizeof(int), &b, sizeof(int));
        ret = tcmapget(mymap, &a, sizeof(int), &c);
        printf("ret=%d sp=%d\n", *ret, c);

        fdi.fd  = 3;
        fdi.dev = 2;
        fdi.is_remote = false;
        fdi.group = 103;
        tcmapput(mymap, &d, sizeof(int), &fdi, sizeof(struct fdinfo));
        f = tcmapget(mymap, &d, sizeof(int), &e);
        printf("fdinfo->group=%d size=%d\n", f->group, e);

        tcmapdel(mymap);
    }

    {
        TCMPOOL *mypool = tcmpoolnew();
        struct fdinfo *f;
        int i=0;
        for(i=0;i<10;i++){
            f = tcmpoolmalloc(mypool, sizeof(struct fdinfo));
            f->fd = i;
            f->is_remote = true;
            f->group = 100;
            printf("f->fd=%d\n", f->fd);
        }
        tcmpooldel(mypool);
    }

    return 0;
}
