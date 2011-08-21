#include <stdio.h>
#include <stdlib.h> // atoi

int main(int argc, char **argv){
    printf("arg count = %d\n", argc);
    if(argc != 2){
        printf("arg count is not 2.\n");
        return -1;
    }
    printf("argv[1] = %s\n", argv[1]);
    printf("atoi(argv[1]) = %d\n",  atoi(argv[1]));
    printf("atol(argv[1]) = %Ld\n", (unsigned long long)atol(argv[1]));
    return 0;
}
