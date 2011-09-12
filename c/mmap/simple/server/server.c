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

#include <sys/mman.h>

int main(int argc, char **argv)
{
    int fd,i,*base,write=0,*ptr=0,offset=0;
    char p='X';
    char *buf;
    size_t size=4*1024;
    //void *base;
    const char path[] = "/tmp/simple.mmap";

    if(1 < argc){
        write  = 1;
        offset = atoi(argv[1]);
        fprintf(stdout,"INFO:  write mode. offset = %d\n", offset);
    }

    if(write){
        fd = open(path,O_RDWR|O_CREAT|O_TRUNC,0666);
    }
    else{
        fd = open(path,O_RDWR,0666);
    }
    if(fd < 0){
        fprintf(stderr,"ERROR: open %s: %s\n",path,strerror(errno));
        goto error;
    }

    if(write && ftruncate(fd,(off_t)size) != 0){
        fprintf(stderr,"ERROR: ftruncate %s: %s\n",path,strerror(errno));
        goto error;
    }

    //base = (int *)mmap(0,size,PROT_READ|PROT_WRITE,MAP_SHARED,fd,(off_t)0);
    base = (char *)mmap(0,size,PROT_READ|PROT_WRITE,MAP_SHARED,fd,(off_t)0);
    if( MAP_FAILED == base ){
        fprintf(stderr,"ERROR: mmap %s: %s\n",path,strerror(errno));
        goto error;
    }

    for(i=0;i<10;i++){
        ptr = base + (int)sizeof(char)*i;
        if(write){
            //offset += i;
            //memcpy(ptr, &offset, sizeof(int));
            //memcpy(ptr, &i, sizeof(int));
            //memcpy(base, &p, sizeof(char));
            memcpy(ptr, &p, sizeof(char));
        }
        fprintf(stdout,"INFO: [%c]\n", *ptr);
        //fprintf(stdout,"INFO:  %s: *ptr=%d, offset=%d, base[%p], ptr[%p]\n",path,*ptr,offset, base, ptr);
    }

    if(munmap(base,size) != 0){
        fprintf(stderr,"ERROR: munmap %s: %s\n",path,strerror(errno));
        goto error;
    }

    if(close(fd) != 0){
        fprintf(stderr,"ERROR: close %s: %s\n",path,strerror(errno));
        goto error;
    }

    fprintf(stdout, "ok\n");
    return (0);

  error:
    fprintf(stderr, "error exit");
    exit(-1);
}
