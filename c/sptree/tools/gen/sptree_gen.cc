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

typedef struct {
    node_sp_t node;
    int64_t   parent_id;
    int64_t   index;
} mapv_t;

std::vector<std::string> split(const std::string &str, char delim){
    std::istringstream iss(str);
    std::string tmp;
    std::vector<std::string> res;
    while(getline(iss, tmp, delim)) res.push_back(tmp);
    return res;
}

static bool get_sptree_map(std::map<int64_t, mapv_t> &sp_map){
    std::string line;
    char *index[5];
    mapv_t val;
    //vector data;

    while(std::getline(std::cin, line)){
        std::cout << line << std::endl;
    }
    return(true);
}

static bool gen_sptree(int fd){
    std::map<int64_t, mapv_t> sp_map;

    if(!get_sptree_map(sp_map)){
        return(false);
    }

    //fix_sptree_map(sp_map);
    //if(!write_sptree(fd, sp_map)){
    //    return(false);
    //}
    return(true);
}

int main(int argc, const char **argv){
    int rc = EXIT_SUCCESS;
    int fd = -1;

    if(argc != 2){
        rc = EXIT_FAILURE;
        goto finally;
    }

    umask(0111);
    fd = open(argv[1], O_WRONLY|O_APPEND|O_CREAT|O_TRUNC, 0666);
    if(fd < 0){
        fprintf(stderr, "ERROR: open failed(%s): %s\n", argv[1], strerror(errno));
        rc = EXIT_FAILURE;
        goto finally;
    }

    if(!gen_sptree(fd)){
        rc = EXIT_FAILURE;
        goto finally;
    }

  finally:
    if(0 <= fd){
        close(fd);
        fd = -1;
    }

    return rc;
}

