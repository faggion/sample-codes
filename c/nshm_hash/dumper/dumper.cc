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

int myforeach(NShm *n, const void *ptr, const void *ud){
    const value_t *v = (const value_t *)ptr;

    UNUSED(ud);
    UNUSED(n);

    fprintf(stderr, "id = %ld\tprent = %ld\n", v->id, v->parent);
    return 1;
}

int _cmd_attach(const char *nshm_file){
    NShm *n = NULL;
    nshmhash_t *nh = NULL;

    n = nshm_attach(nshm_file);
    if(NULL == n){
        return 0;
    }

    nh = (nshmhash_t *)nshm_get(n, TEST, (int)strlen(TEST));
    if(NULL == nh){
        return 0;
    }

    nshmhash_foreach(n, nh, myforeach, NULL);

    nshm_detach(n);
    return 1;
}

int main(const int argc, const char **argv)
{
    if(argc < 2) goto error;

    if(!_cmd_attach(argv[1])) goto error;
    return EXIT_SUCCESS;

  error:
    std::cout << "error" << std::endl;
    return EXIT_FAILURE;
}

