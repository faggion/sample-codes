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

#define UNUSED(x) ((void)(x))

static int dumper(SpTree *sptree, const node_sp_t *node, void *ud){
    UNUSED(ud);
    if(NULL == sptree || NULL == node) return(-1);

    if(0 <= node->parent_index){
        std::cout << node->id << "\t" << sptree->elements[node->parent_index].id ;
    }
    else {
        std::cout << node->id << "\t-1";
    }
    std::cout << "\t" << node->site_id << "\t" << node->depth << std::endl;
    return(1);
}

int main(int argc, const char **argv){
    int rc = EXIT_SUCCESS;
    SpTree *sptree = NULL;

    if(argc != 2){
        rc = EXIT_FAILURE;
        goto finally;
    }

    sptree = sptree_attach(argv[1]);
    if(NULL == sptree){
        std::cerr << "attach failed: " << argv[1] << std::endl;
        rc = EXIT_FAILURE;
        goto finally;
    }

    std::cout << "#id\tpid\tsite\tdepth"<< std::endl;
    sptree_foreach(sptree, dumper, NULL);

  finally:
    sptree_detach(sptree);
    return rc;
}

