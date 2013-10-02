#ifndef __NSHMHASH_H_
#define __NSHMHASH_H_

#include <stdint.h>
#include <nshm.h>

//typedef int64_t nshmhash_bucket_t;

#ifdef __cplusplus
extern "C" {
#endif

typedef int64_t (*nshmhash_hash_fn)(const void *ptr);
typedef int (*nshmhash_cmp_fn)(const void *ptr1, const void *ptr2);
typedef int (*nshmhash_foreach_fn)(NShm *nshm, const void *ptr, const void *ud);

typedef struct {
    uint32_t count;
    int64_t bucket[];
} nshmhash_t;

extern nshmhash_t *nshmhash_create(NShm *nshm, uint32_t bucket_count);
extern void nshmhash_destroy(NShm *nshm, nshmhash_t *hash);

extern int nshmhash_set(NShm *nshm, nshmhash_t *hash, void *ptr, nshmhash_hash_fn hash_fn);
extern void *nshmhash_get(NShm *nshm, const nshmhash_t *hash, const void *ptr, nshmhash_hash_fn hash_fn, nshmhash_cmp_fn cmp_fn);
extern void nshmhash_foreach(NShm *nshm, const nshmhash_t *hash, nshmhash_foreach_fn func, void *ud);

//extern void nshmhash_remove(NShm *nshm, uint64_t bucket_size, nshmhash_hash_fn fn);

#ifdef __cplusplus
}
#endif

#endif
