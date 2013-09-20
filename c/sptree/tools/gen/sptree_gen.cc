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
    std::vector<std::string> datas;
    char *index[5];
    mapv_t val;

    while(std::getline(std::cin, line)){
        if(!line.compare(0, 1, "#")){
            //std::cerr << "This is comment line: " << line << std::endl;
            continue;
        }

        datas = split(line, '\t');
        if(datas.size() != 3){
            continue;
        }

        val.node.id      = strtol(datas[0].c_str(), NULL, 10);
        val.parent_id    = strtol(datas[1].c_str(), NULL, 10);
        val.node.site_id = strtol(datas[2].c_str(), NULL, 10);

        val.node.depth        = -1;
        val.node.parent_index = -1;
        val.index             = -1;
        sp_map[val.node.id]   = val;
    }
    return(true);
}

static void fix_sptree_map(std::map<int64_t,mapv_t> &sp_map){
    std::map<int64_t,mapv_t>::iterator it;
    std::map<int64_t,mapv_t>::iterator parent_it;
    int ix;

    for(ix = 0, it = sp_map.begin(); it != sp_map.end(); ++it, ix++){
        it->second.index = ix;
    }

    for(it = sp_map.begin(); it != sp_map.end(); ++it){
        parent_it = sp_map.find(it->second.parent_id);

        if(parent_it != sp_map.end()){
            it->second.node.parent_index = parent_it->second.index;
        }
        else{
            it->second.node.parent_index = -1;
        }
    }

    for(it = sp_map.begin(); it != sp_map.end(); ++it){
        int64_t parent_id = it->second.parent_id;

        for(ix = 0; 0 <= parent_id; ix++){
            parent_it = sp_map.find(parent_id);

            if(parent_it != sp_map.end()){
                parent_id = parent_it->second.parent_id;
            }
            else{
                parent_id = -1;
            }
        }

        it->second.node.depth = ix;
    }
    return;
}

static bool write_sptree(int fd,const std::map<int64_t,mapv_t> &sp_map)
{
    sptree_header_t header;
    std::map<int64_t,mapv_t>::const_iterator it;

    memset(&header,'\0',sizeof(header));
    strncpy(header.magic, SPTREE_MAGIC, sizeof(header.magic));

    header.version = SPTREE_VERSION;
    header.replaced = 0;
    header.ctime = time(NULL);

    if(write(fd,&header,sizeof(header)) < 0){
        fprintf(stderr,"ERROR: write header: %s\n", strerror(errno));
        return(false);
    }

    for(it = sp_map.begin(); it != sp_map.end(); ++it){
        if(write(fd, &(it->second.node), sizeof(it->second.node)) < 0){
            fprintf(stderr,"ERROR: write: %s\n",strerror(errno));
            return(false);
        }
    }

    return(true);
}

static bool gen_sptree(int fd){
    std::map<int64_t, mapv_t> sp_map;

    if(!get_sptree_map(sp_map)){
        return(false);
    }

    fix_sptree_map(sp_map);

    if(!write_sptree(fd, sp_map)){
        return(false);
    }

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

