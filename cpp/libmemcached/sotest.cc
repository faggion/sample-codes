#include <iostream>

#include <libmemcached/memcached.h>
#include <string.h>

using namespace std;

static void die(memcached_st *memc, memcached_return rc){
    cerr <<  memcached_strerror(memc, rc) << endl;
    memcached_free(memc);
    exit(-1);
}

int main(void){
    struct memcached_st *memc;
    struct memcached_server_st *servers;
    memcached_return rc;
    char host[] = "localhost";
    const char key[] = "foo";
    const char val[] = "baz";
    char *value;  
    size_t value_length;
    uint32_t flags;
    uint64_t behave_val = 1;
    int i;

    memc = memcached_create(NULL);

    servers = memcached_server_list_append(NULL, "127.0.0.1", 12211, &rc); 
    //servers = memcached_server_list_append(servers, "127.0.0.1", 12211, &rc); 
    rc = memcached_server_push(memc, servers);

    if(rc != MEMCACHED_SUCCESS) {
        die(memc, rc);
    }

    // 非同期
    rc = memcached_behavior_set(memc, MEMCACHED_BEHAVIOR_NO_BLOCK, behave_val);
    if(rc != MEMCACHED_SUCCESS) {
        die(memc, rc);
    }

    // set
    for(i=0;i<10000;i++){
        rc= memcached_set(memc,key,strlen(key),val,strlen(val),
                          (time_t)0,(uint32_t)0);
        if (rc != MEMCACHED_SUCCESS && rc != MEMCACHED_BUFFERED) {  
            die(memc, rc);
        }
    }
    //// get
    //value= memcached_get(memc, key, strlen(key), &value_length, &flags, &rc);
    //if (rc != MEMCACHED_SUCCESS) {
    //    die(memc, rc);
    //}  
    //cout << "OK:" << value << endl;

    memcached_server_list_free(servers);  
    memcached_free(memc);
    return 0;
}
