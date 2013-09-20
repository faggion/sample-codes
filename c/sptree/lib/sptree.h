#ifndef __SPTREE_H__
#define __SPTREE_H__

#include <stdint.h>
#include <time.h>

#define SPTREE_MAGIC "__sptree__"
#define SPTREE_VERSION 1

typedef struct {
    int64_t id;
    int32_t depth;
    int64_t parent_index;
    int64_t site_id;
} node_sp_t;

typedef struct {
    int _fd;
    size_t _size;
    void *_base;
    int64_t element_count;
    node_sp_t *elements;
} SpTree;

typedef struct {
    char magic[32];
    int16_t version;
    int16_t replaced;
    time_t ctime;
} sptree_header_t;

typedef int (*sptree_for_func_t)(SpTree*, const node_sp_t*, void*);

#ifdef __cplusplus
extern "C" {
#endif

extern SpTree* sptree_attach(const char *path);
extern SpTree* sptree_reattach(SpTree *sptree, const char *path);
extern void    sptree_detach(SpTree *sptree);

extern time_t sptree_get_ctime(SpTree *sptree);
extern int sptree_is_replaced(SpTree *sptree);
extern int sptree_set_replaced(SpTree *sptree);

extern const node_sp_t* sptree_get_node(SpTree *sptree, int64_t id);
extern const node_sp_t* sptree_get_parent(SpTree *sptree, node_sp_t *cur);

extern void sptree_foreach(SpTree *sptree, sptree_for_func_t func, void *udf);

#ifdef __cplusplus
}
#endif
#endif
