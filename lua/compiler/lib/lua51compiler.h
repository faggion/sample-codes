#ifndef __LUA51COMPILER_H_
#define __LUA51COMPILER_H_

#include <stdio.h>
#include <lua.h>

typedef struct {
    size_t buf_size;
    size_t size;
    char  *buf;
} lua_bin_t;

#ifdef __cplusplus
extern "C" {
#endif

lua_bin_t*  lua51_compiler_new_bin();
extern int  lua51_compiler_compile(lua_State *L, const char *code, const char *name, lua_bin_t *bin);
extern void lua51_compiler_free_bin(lua_bin_t *bin);

#ifdef __cplusplus
}
#endif

#endif
