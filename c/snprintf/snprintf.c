#include <stdio.h>
#include <string.h>
#include <time.h>

#define bufsiz 32

int main (void){
    time_t now;
    unsigned long ulong_value;
    char buf[bufsiz] = {0};
    int i;

    time(&now);
    fprintf(stdout, "now %ld\n", now);
    ulong_value = (unsigned long)now;

    for(i=0;i<10;i++){
        snprintf(buf, sizeof(buf), "/dev/foo.%d", i);
        fprintf(stdout, "OK: buf => %s\n", buf);
    }

    const int n = snprintf(NULL, 0, "%lu", ulong_value);
    fprintf(stdout, "ulong_value's string size => %d\n", n);
    char buf2[n+1];
    int c = snprintf(buf, n+1, "%lu", ulong_value);
    fprintf(stdout, "buf=%s\n", buf);

    return 0;
}
