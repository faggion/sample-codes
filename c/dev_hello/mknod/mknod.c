#include <stdio.h>
#include <fcntl.h>
#include <errno.h>
#include <sys/stat.h>

#define MAJOR 280
#define MINOR 512

// MINOR=0
// device dev[71680],sizeof(dev_t)[8],sizeof(unsigned long long)[8],sizeof(u_long)[4]

// MINOR=1
// device dev[71681],sizeof(dev_t)[8],sizeof(unsigned long long)[8],sizeof(u_long)[4]

// MINOR=255
// device dev[71935],sizeof(dev_t)[8],sizeof(unsigned long long)[8],sizeof(u_long)[4]

// % perl -e 'warn 280<<8'
// 71680 at -e line 1.

// MINOR=256
// device dev[1120256],sizeof(dev_t)[8],sizeof(unsigned long long)[8],sizeof(u_long)[4]

// MINOR=511
// device dev[1120511],sizeof(dev_t)[8],sizeof(unsigned long long)[8],sizeof(u_long)[4]

// MINOR=512
// device dev[2168832],sizeof(dev_t)[8],sizeof(unsigned long long)[8],sizeof(u_long)[4]

// MINOR=4095
// device dev[15800575],sizeof(dev_t)[8],sizeof(unsigned long long)[8],sizeof(u_long)[4]

// MINOR=4096
// device dev[16848896],sizeof(dev_t)[8],sizeof(unsigned long long)[8],sizeof(u_long)[4]

// ロジックは/usr/src/linux-headers-2.6.38-10/include/linux/kdev_t.hにあるっぽい

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
    fprintf(stderr, "device dev[%llu],sizeof(dev_t)[%d],sizeof(unsigned long long)[%d],sizeof(u_long)[%d]\n",
            (unsigned long long)dev,
            sizeof(dev_t),
            sizeof(unsigned long long),
            sizeof(u_long));

    fprintf(stderr, "mknod ret[%d] errno[%d]\n", ret, errno);
    return 0;
}
