#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <nshm.h>

#define PATH "/tmp/sample.nshm"
#define SIZE 1024*256

typedef struct _test_struct {
    int  id;
    char name[20];
} test_struct;

int get_nshm(const char *key){
    /* 宣言 */
    test_struct *ts2;
    NShm* n;

    n  = nshm_attach(PATH);
    ts2 = (test_struct *)nshm_get(n, key, (int)strlen(key));
    fprintf(stderr, "id[%d], name[%s]\n", ts2->id, ts2->name);
    nshm_detach(n);

    return 0;
}

int set_nshm(const char *key, const char *val){
    /* 宣言 */
    test_struct *ts, *ts2;
    NShm* n;
    int ret;

    n  = nshm_create(PATH, SIZE, 0666);

    ts = (test_struct *)nshm_memalloc(n, sizeof(test_struct));
    ts->id = 100;
    strcpy(ts->name, val);

    ret = nshm_set(n, key, (int)strlen(key), (const void *)ts);
    fprintf(stderr, "ret[%d]\n", ret);

    nshm_detach(n);

    n  = nshm_attach(PATH);
    ts2 = (test_struct *)nshm_get(n, key, (int)strlen(key));
    fprintf(stderr, "id[%d], name[%s]\n", ts2->id, ts2->name);
    nshm_detach(n);

    return 0;
}

int main(int argc, const char **argv){
    if(argc < 3){
        goto error;
    }

    if(!strcmp("get", argv[1]) &&
       0 < strlen(argv[2])){
        return get_nshm(argv[2]);
    }
    else if(!strcmp("set", argv[1]) &&
            0 < strlen(argv[2]) &&
            0 < strlen(argv[3])){
        return set_nshm(argv[2], argv[3]);
    }
    else{
        goto error;
    }
  error:
    fprintf(stderr, "./sample get $KEY or ./sample set $KEY $VAL\n");
    return -1;
}
