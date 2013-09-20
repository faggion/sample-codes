#include <sys/types.h>
#include <sys/stat.h>
#include <sys/mman.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <fcntl.h>
#include <time.h>
#include <unistd.h>

#include "sptree.h"

static void _sptree_init(SpTree *sptree);

static void _sptree_init(SpTree *sptree){
    memset(sptree,'\0', sizeof(*sptree));
    sptree->_fd = -1;
    sptree->_size = 0;
    sptree->_base = MAP_FAILED;
    sptree->element_count = 0;
    sptree->elements = NULL;
    return;
}
static int _cmp_spnode(const void *s1, const void *s2){
    const node_sp_t *node1 = (const node_sp_t*)s1;
    const node_sp_t *node2 = (const node_sp_t*)s2;
    return (int)(node1->id - node2->id);
}

SpTree* sptree_attach(const char *path){
    SpTree *sptree = NULL;
    sptree_header_t *header;
    struct stat st;
    char *ptr;

    if(NULL == path) goto error;

    sptree = (SpTree*)malloc(sizeof(*sptree));
    if(NULL == sptree){
        fprintf(stderr, "ERROR: malloc failed: %s\n", strerror(errno));
        goto error;
    }

    _sptree_init(sptree);

    sptree->_fd = open(path, O_RDWR);
    if(sptree->_fd < 0){
        fprintf(stderr, "ERROR: open(%s): %s\n", path, strerror(errno));
        goto error;
    }

    if(fstat(sptree->_fd, &st) < 0){
        fprintf(stderr, "ERROR: fstat(%s): %s\n", path, strerror(errno));
        goto error;
    }

    sptree->_size = (size_t)st.st_size;
    sptree->_base = mmap(0, sptree->_size, PROT_READ|PROT_WRITE, MAP_SHARED, sptree->_fd, (off_t)0);
    if(MAP_FAILED == sptree->_base){
        fprintf(stderr, "ERROR: mmap(%s): %s\n", path, strerror(errno));
        goto error;
    }

    header = (sptree_header_t*)sptree->_base;
    if(strncmp(header->magic, SPTREE_MAGIC, strlen(SPTREE_MAGIC)) != 0){
        fprintf(stderr, "ERROR: magic error: %s\n", path);
        goto error;
    }

    if(header->version != SPTREE_VERSION){
        fprintf(stderr, "ERROR: version error: %s\n", path);
        goto error;
    }

    ptr = (char*)(sptree->_base);
    sptree->element_count = (int64_t)((sptree->_size - sizeof(sptree_header_t))/sizeof(node_sp_t));
    sptree->elements = (node_sp_t*)(ptr + sizeof(sptree_header_t));
    return(sptree);

  error:
    sptree_detach(sptree);
    return(NULL);
}

void sptree_detach(SpTree *sptree){
    if(NULL == sptree) return;

    if(sptree->_base != MAP_FAILED){
        munmap(sptree->_base, sptree->_size);
        sptree->_base = MAP_FAILED;
    }

    if(0 <= sptree->_fd){
        close(sptree->_fd);
        sptree->_fd = -1;
    }
    free(sptree);
    return;
}

SpTree* sptree_reattach(SpTree *sptree, const char *path){
    sptree_detach(sptree);
    return(sptree_attach(path));
}

time_t sptree_get_ctime(SpTree *sptree){
    sptree_header_t *header;
    if(NULL == sptree) return(0);
    header = (sptree_header_t*)sptree->_base;
    return(header->ctime);
}

int sptree_is_replaced(SpTree *sptree){
    sptree_header_t *header;
    if(NULL == sptree) return(0);

    header = (sptree_header_t *)sptree->_base;
    return(header->replaced);
}

int sptree_set_replaced(SpTree *sptree){
    sptree_header_t *header;
    if(NULL == sptree) return(0);

    header = (sptree_header_t *)sptree->_base;
    return((header->replaced = 1));
}

const node_sp_t* sptree_get_node(SpTree *sptree, int64_t id){
    node_sp_t dummy;
    if(NULL == sptree) return(NULL);

    dummy.id = id;
    return ((const node_sp_t*)(bsearch(&dummy, sptree->elements, (size_t)sptree->element_count, sizeof(node_sp_t), _cmp_spnode)));
}

const node_sp_t* sptree_get_parent(SpTree *sptree, node_sp_t *current_node){
    if(NULL == sptree || NULL == current_node || current_node->parent_index < 0) return(NULL);
    return(&sptree->elements[current_node->parent_index]);
}

void sptree_foreach(SpTree *sptree, sptree_for_func_t func, void *udf){
    int ix;
    if(NULL == sptree || NULL == func) return;

    for(ix=0; ix < sptree->element_count; ix++){
        if(!func(sptree, &sptree->elements[ix], udf)){
            return;
        }
    }
}


