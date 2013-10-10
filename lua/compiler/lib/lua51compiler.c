#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <errno.h>
#include <stdint.h>
#include <fcntl.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <time.h>
#include <libgen.h>

#include <lua.h>
#include <lualib.h>
#include <lauxlib.h>

#include "lua51compiler.h"

#define _BYTECODE_FIRST_SIZ 1024
#define UNUSED(x) ((void)(x))
#define DBG 1

static int _save_bin(lua_State *L, const void* p, size_t sz, void* ud);
static int _expand_bin_buf(lua_bin_t *bin, size_t add);
//static void _dump_bin(lua_bin_t *bin){
//    if(bin == NULL) return;
//    if(DBG) fprintf(stderr, "bin size = %ld, bin buf size = %ld\n", bin->size, bin->buf_size);
//}

int lua51_compiler_compile(lua_State *L, const char *code, const char *name, lua_bin_t *bin){
    int top, cur, ret;

    if(NULL == L || NULL == code || NULL == name || NULL == bin) return 1;

    top = lua_gettop(L);

    ret = luaL_loadbuffer(L, code, strlen(code), name);
    if( ret != 0 ){
        if(DBG) fprintf(stderr, "load buffer error\n");
        goto error;
    }

    ret = lua_dump(L, _save_bin, bin);
    if( ret != 0 ){
        if(DBG) fprintf(stderr, "dump error\n");
        goto error;
    }
    return 0;

  error:
    cur = lua_gettop(L);
    if(DBG) fprintf(stderr, "ERROR: top = %d, cur = %d\n", top, cur);
    lua_pop(L, top - cur);
    return 1;
}

lua_bin_t* lua51_compiler_new_bin(){
    lua_bin_t *bin = NULL;

    bin = (lua_bin_t *)malloc(sizeof(lua_bin_t));
    if(NULL == bin) return NULL;

    bin->buf  = (char *)malloc(_BYTECODE_FIRST_SIZ);
    if(NULL == bin->buf) goto error;

    bin->size = 0;
    bin->buf_size = _BYTECODE_FIRST_SIZ;
    return bin;

  error:
    lua51_compiler_free_bin(bin);
    return NULL;
}
void lua51_compiler_free_bin(lua_bin_t *bin){
    if(NULL != bin){
        free(bin->buf);
        free(bin);
    }
    return;
}

static int _save_bin(lua_State *L, const void* p, size_t size, void* ud){
    lua_bin_t *bin = (lua_bin_t *)ud;

    if(NULL == L || NULL == ud) return 1; 

    if(_expand_bin_buf(bin, size) != 0) return 1;

    memcpy(&bin->buf[bin->size], p, size);
    bin->size += size;

    return 0;
}

static int _expand_bin_buf(lua_bin_t *bin, size_t add){
    char *tmp = NULL;
    if(NULL == bin) return 1;

    if(add < 1 || bin->size + add < bin->buf_size) return 0; // not need to expand

    tmp = bin->buf;

    bin->buf = (char *)realloc(bin->buf, bin->buf_size + add);

    if(NULL == bin->buf){
        free(tmp);
        return 1;
    }
    bin->size += add;
    return 0; // expantion success
}
