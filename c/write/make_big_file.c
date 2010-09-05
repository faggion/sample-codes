#include <stdio.h>

int main(){
    FILE *fd;
    int i=0;
    //const char line[] = "aaaaaaaa";

    fd = fopen("./bigfile", "w");
    for(i=0;i<128*1024*10;i++){
        fputs("aaaaaaaa",fd);
    }
    fclose(fd);

    return 0;
}
