#include <nshm.h>
#include "nshmhash.h"
#include <stdio.h>

typedef struct {
    int64_t offset;
    int64_t next;
} nshmhash_bucket_node_t;

nshmhash_t* nshmhash_create(NShm *nshm, uint32_t bucket_count){
    nshmhash_t *hash = NULL;
    int ix;

    if(NULL == nshm) return NULL;

    hash = (nshmhash_t*)nshm_memalloc(nshm, (int32_t)(sizeof(nshmhash_t) + sizeof(int64_t) * bucket_count));
    if(NULL == hash) return NULL;

    hash->count = bucket_count;
    for(ix=0; ix<(int)hash->count; ix++){
        hash->bucket[ix] = -1;
    }
    return hash;
}

void nshmhash_destroy(NShm *nshm, nshmhash_t *hash){
    if(NULL != nshm){
        nshm_memfree(nshm, hash);
        hash = NULL;
    }
    return;
}

int nshmhash_set(NShm *nshm, nshmhash_t *hash, void *ptr, nshmhash_hash_fn hash_fn){
    void *_nshm_base = NULL;
    nshmhash_bucket_node_t *bn = NULL;
    int bucket_idx;

    if(NULL == nshm || NULL == hash || NULL == ptr) return 0;
    SET_NSHMBASE(nshm);

    bn = (nshmhash_bucket_node_t*)nshm_memalloc(nshm, (int32_t)sizeof(nshmhash_bucket_node_t));
    if(NULL == bn) return 0;

    bucket_idx = (int)(hash_fn(ptr) % hash->count);
    bn->next   = hash->bucket[bucket_idx];
    bn->offset = vos_assign(int64_t, ptr);
    hash->bucket[bucket_idx] = vos_assign(int64_t, bn);
    return 1;
}

void* nshmhash_get(NShm *nshm, const nshmhash_t *hash, const void *ptr, nshmhash_hash_fn hash_fn, nshmhash_cmp_fn cmp_fn){
    void *_nshm_base = NULL;
    void *val = NULL;
    int bucket_idx;
    int64_t cursor;
    nshmhash_bucket_node_t *bn = NULL;

    if( NULL == nshm || NULL == hash || NULL == ptr || NULL == cmp_fn ){
        return(NULL);
    }

    SET_NSHMBASE(nshm);
    bucket_idx = (int)(hash_fn(ptr) % hash->count);
    cursor = hash->bucket[bucket_idx];
    while(0 <= cursor){
        bn  = vos_ptr(nshmhash_bucket_node_t*, cursor);
        val = vos_ptr(void*, bn->offset);
        if(cmp_fn(ptr, val) == 0){
            return(val);
        }
        cursor = bn->next;
    }
    return(NULL);
}

void nshmhash_foreach(NShm *nshm, const nshmhash_t *hash, nshmhash_foreach_fn func, void *ud)
{
    void *_nshm_base = NULL;
    int64_t cursor;
    int ix;
    nshmhash_bucket_node_t *bn = NULL;

    if( NULL == nshm || NULL == hash || NULL == func ){
        return;
    }

    SET_NSHMBASE(nshm);
    for(ix=0; ix< (int)hash->count; ix++){
        cursor = hash->bucket[ix];
        while( cursor >= 0 ){
            bn = vos_ptr(nshmhash_bucket_node_t*, cursor);
            if( !func(nshm, vos_ptr(void*, bn->offset), ud) ){
                return;
            }
            cursor = bn->next;
        }
    }
    return;
}
