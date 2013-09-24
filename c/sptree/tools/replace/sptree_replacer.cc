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

#include "sptree.h"

int main(int argc, const char **argv){
    int rc = EXIT_SUCCESS;
    SpTree *sptree_old = NULL;
    SpTree *sptree_new = NULL;

    if(argc != 3){
        rc = EXIT_FAILURE;
        goto finally;
    }

    sptree_old = sptree_attach(argv[2]);
    if(NULL == sptree_old){
        std::cerr << "old shm attach failed: " << argv[2] << std::endl;
        rc = EXIT_FAILURE;
        goto finally;
    }
    sptree_new = sptree_attach(argv[1]);
    if(NULL == sptree_old){
        std::cerr << "new shm attach failed: " << argv[1] << std::endl;
        rc = EXIT_FAILURE;
        goto finally;
    }

    if(rename(argv[1],argv[2]) < 0){
        std::cerr << fprintf(stderr,"ERROR: rename failed(%s->%s): %s",argv[1],argv[2],strerror(errno)) << std::endl;
        rc = EXIT_FAILURE;
        goto finally;
    }

    sptree_set_replaced(sptree_old);

  finally:
    sptree_detach(sptree_new);
    sptree_detach(sptree_old);
    return rc;
}

