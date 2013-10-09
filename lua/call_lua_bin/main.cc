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
#include <fstream>
#include <vector>
#include <string>
#include <map>

#define UNUSED(x) ((void)(x))

static size_t size = 0;

int _exec_lua(const char *file){
    lua_State *L = NULL;
    int top, ret, n, rc=0;
    std::string line;
    std::ifstream ifs(file);
    std::string content((std::istreambuf_iterator<char>(ifs)),
                        (std::istreambuf_iterator<char>()));

    L = luaL_newstate();
    luaL_openlibs(L);
    top = lua_gettop(L);
    ret = luaL_loadbuffer(L, content.c_str(), content.size(), "sample_name");
    if( ret != 0 ){
        std::cerr << "error1: " << ret << std::endl;
        lua_pop(L, 1);
        return(rc);
    }

    ret = lua_pcall(L, 0, LUA_MULTRET, 0);
    if( ret != 0 ){
        std::cerr << "error2: "     << ret << std::endl;
        std::cerr << "LUA_ERRRUN: " << LUA_ERRRUN << std::endl;
        std::cerr << "LUA_ERRMEM: " << LUA_ERRMEM << std::endl;
        std::cerr << "LUA_ERRERR: " << LUA_ERRERR << std::endl;
        lua_pop(L, 1);
        return(rc);
    }

    n = lua_gettop(L) - top;
    if( n > 0 ){
        switch(lua_type(L, -1)){
        case LUA_TBOOLEAN:
            rc = (int)lua_toboolean(L, -1);
            break;
        case LUA_TNUMBER:
            rc = (int)lua_tointeger(L, -1);
            break;
        default:
            break;
        }
        lua_pop(L, n);
    }
    std::cerr << "return code = " <<  rc << std::endl;

    return 0;
}

// NOTICE: この関数は何度も呼ばれる
static int _write(lua_State *L, const void* p, size_t sz, void* ud){
    char *buf = NULL;
    int i=0;

    UNUSED(ud);
    if(NULL == L) return 1;

    //std::cerr << "size: " << sz << std::endl;
    size += sz;

    buf = (char *)malloc(sz);
    if(NULL == buf) return 1;
    memcpy(buf, p, sz);
    //buf[sz] = '\0';

    //std::cout << buf;
    for(i=0;i<(int)sz;i++){
        printf("%c", buf[i]);
    }
    
    free(buf);
    return(0);
}

int _compile(const char *file){
    lua_State *L = NULL;
    int top, ret, rc=0;
    std::string line;
    std::string buf;
    std::ifstream ifs(file);
    std::string content((std::istreambuf_iterator<char>(ifs)),
                        (std::istreambuf_iterator<char>()));
    //std::cerr << content << std::endl;
    //std::cerr << content.size() << std::endl;

    L = luaL_newstate();
    luaL_openlibs(L);
    top = lua_gettop(L);
    ret = luaL_loadbuffer(L, content.c_str(), content.size(), "sample_name");
    if( ret != 0 ){
        std::cerr << "error1" << std::endl;
        lua_pop(L, 1);
        return(rc);
    }

    ret = lua_dump(L, _write, NULL);
    if( ret != 0 ){
        lua_pop(L, 1);
    }

    std::cerr << "inc size = " << size << std::endl;
    return(0);
}

int main(int argc, const char **argv){
    int rc = EXIT_SUCCESS;

    if(argc == 3 && !strcmp(argv[1], "rawexec") && _exec_lua(argv[2]) == 0){
        return rc;
    }
    else if(argc == 3 && !strcmp(argv[1], "compile") && _compile(argv[2]) == 0){
        return rc;
    }
    rc = EXIT_FAILURE;
    goto finally;

  finally:
    std::cerr << "Error" << std::endl;
    return rc;
}
