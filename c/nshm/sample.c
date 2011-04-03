#include <stdio.h>
#include <string.h>
#include <nshm.h>

#define PATH "/tmp/sample.nshm"
#define SIZE 1024*256

typedef struct _test_struct {
    long key;
    double val;
    char name[20];
} test_struct;

int get_nshm(const char *key){
    NShm *n;
    int *ret;
    n = nshm_attach(PATH);
    const char k[] = "foo";
    //fprintf(stderr, "ret[%s]\n", (const char *)nshm_get(n, key, (int)strlen(key)+1));
    //fprintf(stderr, "ret[%s]\n", (const char *)nshm_get(n, k, (int)strlen(k)+1));
    //fprintf(stderr, "ret[%s]\n", (const char *)nshm_get(n, key, 4));
    //fprintf(stderr, "ret[%d]\n", (int)nshm_get(n, key, (int)strlen(k)+1));
    ret = (int *)nshm_get(n, key, (int)strlen(key)+1);
    fprintf(stderr, "ret[%d]\n", ret);
    nshm_detach(n);
    return 0;
}

int set_nshm(const char *key, const char *val){
    int ret;
    NShm* n;
    n   = nshm_create(PATH, SIZE, 0666);
    ret = nshm_set(n, key, (int)strlen(key)+1, (const void *)vint);
    fprintf(stderr, "ret[%d], key[%s], vint[%d]\n", ret, key, vint);
    fprintf(stderr, "ret[%d]\n", (int)nshm_get(n, key, (int)strlen(key)+1));

    nshm_detach(n);
    n = nshm_attach(PATH);

    fprintf(stderr, "ret[%d]\n", (int)nshm_get(n, key, (int)strlen(key)+1));
    //fprintf(stderr, "ret[%s]\n", (const char *)nshm_get(n, key, (int)strlen(key)+1));
    */

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
