#include <stdio.h>
#include <fcntl.h>
#include <nshm.h>

typedef struct _test_struct {
    long key;
    double val;
    char name[20];
} test_struct;

int main(void){
    test_struct ts;
    ts.key = 1;
    ts.val = ts.key + 10.0;
    fprintf(stderr, "key[%d], val[%f]\n", ts.key, ts.val);
    fprintf(stderr, "size of test_struct[%d]\n", sizeof(test_struct));
    return 0;
}
