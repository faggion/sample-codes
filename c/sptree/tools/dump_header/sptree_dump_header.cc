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
    SpTree *sptree = NULL;
    sptree_header_t *sph = NULL;

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

    std::cout << "element_count:\t" << sptree->element_count << std::endl;

    sph = (sptree_header_t *)sptree->_base;

    std::cout << "hdr magic:\t"   << sph->magic   << std::endl;
    std::cout << "hdr version:\t" << sph->version << std::endl;
    std::cout << "hdr replaced:\t"  << sph->replaced << std::endl;
    std::cout << "hdr ctime:\t"   << sph->ctime << std::endl;

    //sptree_foreach(sptree, dumper, NULL);

  finally:
    sptree_detach(sptree);
    return rc;
}

