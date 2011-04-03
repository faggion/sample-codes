#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct _test_struct {
    int key;
    double val;
} test_struct;

typedef struct _str_struct {
    int id;
    char name[20];
} str_struct;

int do_test_struct(test_struct *ts){
    ts->key = 1;
    ts->val = ts->key + 10.0;
    fprintf(stderr, "key[%d], val[%f]\n", ts->key, ts->val);
    return 0;
}

int main(void){
    test_struct *ts;
    str_struct ss;
    //char name[20] = "tanarky";
    char *str;

    ts = (test_struct *)malloc(sizeof(test_struct));
    do_test_struct(ts);
    free(ts);

    str = (char *)malloc(sizeof(char) * 20);
    free(str);

    ss.id = 10;
    memset(ss.name, 0, sizeof(char) * 20);
    //memcpy(ss.name, name, 20);
    strcpy(ss.name, "tanarky");

    return 0;
}
