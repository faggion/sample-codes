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

int main (int argc, char **argv){
    TCMAP *mymap = tcmapnew();
    int a,b,*ret,c,d;
    a = 10;
    b = 100;

    tcmapput(mymap, &a, sizeof(int), &b, sizeof(int));
    ret = (int *)tcmapget(mymap, &a, sizeof(int), &c);

    printf("ret=%d sp=%d\n", *ret, c);
    tcmapdel(mymap);
    return 0;
}
