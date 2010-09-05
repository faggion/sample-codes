#include <stdio.h>

int main(){
    printf("pagesize=%d\n", getpagesize());
    printf("sizeofvoidp=%d\n", sizeof(void *));
    printf("sizeofint=%d\n", sizeof(int));
    printf("sizeoflong=%d\n", sizeof(long));
    return 0;
}
