#include <stdio.h>

int main(void){
    int a = 10;
    // __sync_bool_compare_and_swap(A,B,C)
    // __sync_add_and_fetch(A,B)
    // __sync_sub_and_fetch(A,B)
    printf("a 1 = %d\n", a);
    printf("a 2 = %d\n", __sync_add_and_fetch(&a, 10));
    printf("a 3 = %d\n", a);
    return 0;
}
