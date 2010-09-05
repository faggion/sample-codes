#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

// FOR O_DIRECT
#define __USE_GNU
//#define _GNU_SOURCE
#include <fcntl.h>

// 参考
// http://search.luky.org/linux-kernel.2003/msg30909.html

int main(int argc, const char **argv){
    char file[]  = "./file";
    int ret,fd,i = 0;
    int min_size = 512;
    if(argc < 3){
        printf("invalid argument\n");
        return -1;
    }
    int n    = atoi(argv[1]);
    int loop = atoi(argv[2]);

    // OK
    void *buffer;
    //posix_memalign(&buffer, getpagesize(), getpagesize());
    posix_memalign(&buffer, min_size*n, min_size*n);

    // OKだけどposix_memalignが推奨らしい
    //void *buffer = (void *)memalign(getpagesize(), getpagesize());

    // mallocはアライメントされないのでだめらしい
    //void *buffer = calloc(getpagesize()/sizeof(char *), sizeof(char *));
    //void *buffer = calloc(getpagesize(), sizeof(char *));
    //void *buffer = malloc(getpagesize());
    //memset(buffer,'*',getpagesize());

    if(buffer == NULL){
        printf("メモリが確保出来ませんでした\n");
        return -1;
    }

    //for(i=0;i<1024;i++){
    for(i=0;i<loop;i++){
        // O_DIRECTのみ
        fd = open(file, O_CREAT | O_RDWR | O_DIRECT, 0666 );

        // O_SYNCをつけるとかなり遅くなる
        //fd = open(file, O_CREAT | O_RDWR | O_DIRECT | O_SYNC, 0666 );
        //fd = open(file, O_CREAT | O_RDWR, 0666 );

        if(fd == -1){
            perror("open");
            return -1;
        }

        // 書き込みサイズは、pagesize(の倍数)じゃないとだめ
        //ret = write(fd, buffer, getpagesize());
        ret = write(fd, buffer, 512);
        if(ret <= 0){
            printf("write error[%d][%s]\n",ret, strerror(errno));
            close(fd);
            return -1;
        }
        close(fd);
    }
    free(buffer);
    return 0;
}
