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

int myforeach(NShm *n, const void *ptr, const void *ud){
    const value_t *v = (const value_t *)ptr;

    UNUSED(ud);
    UNUSED(n);

    fprintf(stderr, "id = %ld\tprent = %ld\n", v->id, v->parent);
    return 1;
}

std::vector<std::string> split(const std::string &str, char delim){
    std::istringstream iss(str);
    std::string tmp;
    std::vector<std::string> res;
    while(getline(iss, tmp, delim)) res.push_back(tmp);
    return res;
}

int _cmd_create(const char *nshm_file){
    NShm *n = NULL;
    std::string line;
    value_t *v = NULL;
    nshmhash_t *nh = NULL;
    std::vector<std::string> datas;

    n = nshm_create(nshm_file, 4096*1024, 0666);
    if(NULL == n) return 0;

    nh = nshmhash_create(n, 1024);
    if(NULL == nh) return 0;

    while(std::getline(std::cin, line)){
        v = (value_t*)nshm_memalloc(n, (int32_t)sizeof(value_t));
        if(!line.compare(0, 1, "#")) continue;
        datas = split(line, ',');
        if(datas.size() != 2) continue;

        v->id     = (int64_t)strtol(datas[0].c_str(), NULL, 10);
        v->parent = (int64_t)strtol(datas[1].c_str(), NULL, 10);
        nshmhash_set(n, nh, (void*)v, myhash);
    }

    nshmhash_foreach(n, nh, myforeach, NULL);

    if(nshm_set(n, TEST, (int)strlen(TEST), (const void*)nh) < 0){
        return 0;
    }

    nshm_detach(n);
    return 1;
}

int main(const int argc, const char **argv)
{
    if(argc < 2) goto error;

    if(!_cmd_create(argv[1])) goto error;
    return EXIT_SUCCESS;

  error:
    std::cout << "error" << std::endl;
    return EXIT_FAILURE;
}

