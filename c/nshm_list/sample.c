#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <nshm.h>

#define PATH "/tmp/space.nshm"
#define SIZE 1024*256

typedef struct _item {
    int id;
    int price;
    int next;
} item;

int init(const char *key){
    void *_nshm_base=NULL;
    item *it;
    item *it_tmp=NULL;
    NShm *n;
    int i, ret;

    n  = nshm_create(PATH, SIZE, 0666);
    fprintf(stderr, "size of item: %d\n", sizeof(item));
    SET_NSHMBASE(n);
    for(i=0;i<10;i++){
        it = (item *)nshm_memalloc(n, sizeof(item));
        it->id    = i;
        it->price = 1000 + i;
        if(it_tmp != NULL){
            it->next = vos_assign(int, it_tmp);
            fprintf(stderr, "next ptr [%d][%d]\n", it->id, it->next);
        }
        it_tmp = it;
    }
    ret = nshm_set(n, key, (int)strlen(key), (const void *)it);
    //fprintf(stderr, "ret[%d]\n", ret);
    nshm_detach(n);
    return 0;
}

int dump(const char *key){
    void *_nshm_base=NULL;
    item *it;
    NShm *n;

    n  = nshm_attach(PATH);
    it = (item *)nshm_get(n, key, (int)strlen(key));
    SET_NSHMBASE(n);
    do {
        fprintf(stderr, "item id[%d],price[%d]\n", it->id, it->price);
        it = vos_ptr(item *, it->next);
    } while(it->next);
    nshm_detach(n);
    return 0;
}

int main(int argc, const char **argv){
    if(argc < 2){
        goto error;
    }

    if(2 < argc &&
       !strcmp(argv[1], "init")){
        init(argv[2]);
        return 0;
    }
    else if(2 < argc &&
            !strcmp(argv[1], "dump")){
        dump(argv[2]);
        return 0;
    }
    goto error;

  error:
    fprintf(stderr, "error\n");
    return -1;
}
