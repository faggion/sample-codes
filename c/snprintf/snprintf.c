#include <stdio.h>
#include <string.h>

#define bufsiz 32

int main (void){
    char buf[bufsiz];
    int i;

    for(i=0;i<10;i++){
        snprintf(buf, sizeof(buf), "/dev/foo.%d", i);
        fprintf(stdout, "OK: buf => %s\n", buf);
    }
    return 0;
}
