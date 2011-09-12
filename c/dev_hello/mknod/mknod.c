#include <stdio.h>
#include <fcntl.h>
#include <errno.h>
#include <sys/stat.h>

#define MAJOR 280
#define MINOR 1

int main(void)
{
    const char path[] = "/dev/hello_dev.1";
    int ret;
    dev_t dev = makedev(MAJOR, MINOR);

    // S_IFCHR = character special
    // 0666だけどwritableにならないのが謎
    ret = mknod(path, S_IFCHR | 0666, dev);

    // /usr/include/linux/coda.h
    // dev_tは数値(typedef u_long dev_t)で、(MAJOR << 8 | MINOR)である
    // ただ、sizeof(dev_t)とsizeof(u_long)が違うのが謎
    fprintf(stderr, "device dev[%ld],sizeof(dev_t)[%d],sizeof(long)[%d]\n",
            (u_long)dev,
            sizeof(dev_t),
            sizeof(u_long));

    fprintf(stderr, "mknod ret[%d] errno[%d]\n", ret, errno);
    return 0;
}
