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

int _exec_lua(){
    lua_State *L = NULL;
    int top, ret, n, rc=0;
    std::string line;
    std::string buf;
    while(std::getline(std::cin, line)){
        buf += line + "\n"; // FIXME
    }
    //std::cerr << buf << std::endl;

    L = luaL_newstate();
    luaL_openlibs(L);
    top = lua_gettop(L);
    ret = luaL_loadbuffer(L, buf.c_str(), strlen(buf.c_str()), "sample_name");
    if( ret != 0 ){
        std::cerr << "error1" << std::endl;
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

int main(int argc, const char **argv){
    int rc = EXIT_SUCCESS;

    if(_exec_lua() == 0){
        return rc;
    }
    rc = EXIT_FAILURE;
    goto finally;

  finally:
    std::cerr << "Error" << std::endl;
    return rc;
}
