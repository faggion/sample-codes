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

#include <lua.hpp>
#include <lualib.h>
#include <lauxlib.h>

#include <sstream>
#include <iostream>
#include <vector>
#include <string>
#include <map>

#define ADSHM_SIZE 4096*1024

static int _exec_lua(const char *file);
static int _func_addition(lua_State *L);
static int _func_subtraction(lua_State *L);

static struct {
    const char *name;
    lua_CFunction func;
} _cmd_funcs[] = {
    {"func_addition",    _func_addition},
    {"func_subtraction", _func_subtraction},
    {NULL, NULL},
};

int main(int argc, const char **argv){
    int rc = EXIT_SUCCESS;

    if(argc == 2 && _exec_lua(argv[1]) == 0){
        return rc;
    }
    rc = EXIT_FAILURE;
    goto finally;

  finally:
    std::cerr << "Error" << std::endl;
    return rc;
}

static int _func_addition(lua_State *L){
    int a = 0;
    int b = 0;

    a = (int)lua_tointeger(L, 1);
    b = (int)lua_tointeger(L, 2);

    lua_pushinteger(L, a + b);
    return 1;
}

static int _func_subtraction(lua_State *L){
    int a = 0;
    int b = 0;

    a = (int)lua_tointeger(L, 1);
    b = (int)lua_tointeger(L, 2);

    lua_pushinteger(L, a - b);
    return 1;
}

static int _exec_lua(const char *file){
    int ix, rc = 0;
    lua_State *L = lua_open();

    for(ix=0; _cmd_funcs[ix].name != NULL;ix++){
        lua_register(L, _cmd_funcs[ix].name, _cmd_funcs[ix].func);
    }

    luaL_openlibs(L);
    rc = luaL_dofile(L, file);
    lua_close(L);

    return rc;
}

