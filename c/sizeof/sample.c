#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <pthread.h>
#include <sys/types.h>
#include <time.h>

typedef struct _foo
{
    int id;
    char name[];
} FOO;

int main(void){
    char buf[128];
    int ix=1;
    sprintf(buf, "%d", ix);

    fprintf(stderr, "sizeof(short): %d\n", sizeof(short));
    fprintf(stderr, "sizeof(unsigned short): %d\n", sizeof(unsigned short));
    fprintf(stderr, "sizeof(int): %d\n", sizeof(int));
    fprintf(stderr, "sizeof(unsigned int): %d\n", sizeof(unsigned int));
    fprintf(stderr, "sizeof(char): %d\n", sizeof(char));
    fprintf(stderr, "sizeof(buf) : %d\n", sizeof(buf));
    fprintf(stderr, "sizeof(pthread_spinlock_t): %d\n", sizeof(pthread_spinlock_t));
    fprintf(stderr, "sizeof(int64_t): %d\n", sizeof(int64_t));
    fprintf(stderr, "sizeof(time_t): %d\n", sizeof(time_t));
    fprintf(stderr, "sizeof(sigset_t): %d\n", sizeof(sigset_t));
    fprintf(stderr, "int: %d\n", ((int32_t)-1));
    fprintf(stderr, "align(50): %d\n", ((50 + 8 - 1) & -8));
    fprintf(stderr, "align(16): %d\n", ((16 + 8 - 1) & -8));
    fprintf(stderr, "align(32): %d\n", ((32 + 8 - 1) & -8));
    fprintf(stderr, "align(33): %d\n", ((33 + 8 - 1) & -8));
    fprintf(stderr, "FOO: %d\n", sizeof(FOO));
    fprintf(stderr, "strlen buf: %d\n", strlen(buf));
    return 0;
}
