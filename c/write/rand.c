#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
    int rnd,n=0;
    srand(time(NULL));
    for(n = 0; n < 20; ++n){
        //rnd = rand()/32768;
        rnd = rand()%20480;
        printf("%d\n", rnd);
    }

    return 0;
}
