#include <stdio.h>

int main(void){
    int a = 10;
    printf("a 1 = %d\n", a);
    printf("a 2 = %d\n", __sync_add_and_fetch(&a, 10));
    printf("a 3 = %d\n", a);
    return 0;
}
