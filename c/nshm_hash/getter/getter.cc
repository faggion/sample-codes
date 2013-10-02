#include <sys/types.h>
#include <sys/stat.h>
#include <errno.h>
#include <stdint.h>
#include <fcntl.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <time.h>
#include <stdio.h>
#include <libgen.h>

#include <sstream>
#include <iostream>
#include <vector>
#include <string>
#include <map>

#include "nshm.h"
#include "nshmhash.h"

#define UNUSED(x) ((void)(x))
#define TEST "test"

typedef struct {
    int64_t id;
    int64_t parent;
} value_t;

int64_t myhash(const void *ptr){
    const value_t *v = (const value_t*)ptr;
    return(v->id);
}

int mycmp(const void *ptr1, const void *ptr2){
    const value_t *v1 = (const value_t*)ptr1;
    const value_t *v2 = (const value_t*)ptr2;
    return((int)(v1->id - v2->id));
}

int _cmd_get(const char *nshm_file, int64_t id){
    NShm *n = NULL;
    nshmhash_t *nh = NULL;
    value_t dummy;
    value_t *found = NULL;

    n = nshm_attach(nshm_file);
    if(NULL == n){
        return 0;
    }

    nh = (nshmhash_t *)nshm_get(n, TEST, (int)strlen(TEST));
    if(NULL == nh){
        return 0;
    }

    dummy.id = id;
    found = (value_t *)nshmhash_get(n, nh, &dummy, myhash, mycmp);
    if(found){
        fprintf(stdout, "i found a value: id=%ld, parent=%ld\n", found->id, found->parent);
    }

    nshm_detach(n);
    return 1;
}

int main(const int argc, const char **argv)
{
    if(argc < 2) goto error;

    if(!_cmd_get(argv[1], (int64_t)strtol(argv[2], NULL, 10))) goto error;
    return EXIT_SUCCESS;

  error:
    std::cout << "error" << std::endl;
    return(EXIT_FAILURE);
}

