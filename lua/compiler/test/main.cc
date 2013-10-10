#include <iostream>
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

#include <lua51compiler.h>

#include <sstream>
#include <iostream>
#include <fstream>
#include <string>

#define NAME "sample_name"

int _compile(const char *file){
    int i, rc=-1;
    lua_bin_t *bin = NULL;
    lua_State *L = NULL;

    std::ifstream ifs(file);
    std::string content((std::istreambuf_iterator<char>(ifs)),
                        (std::istreambuf_iterator<char>()));

    if(content.size() < 1) return 0;

    L = luaL_newstate();
    luaL_openlibs(L);

    bin = lua51_compiler_new_bin();
    if(NULL == bin) goto finally;

    if(lua51_compiler_compile(L, content.c_str(), NAME, bin) != 0){
        fprintf(stderr, "compile error!\n");
        goto finally;
    }

    for(i=0; i < (int)bin->size; i++){
        printf("%c", bin->buf[i]);
    }
    rc = 0;

  finally:
    lua51_compiler_free_bin(bin);
    lua_close(L);
    return rc;
}

int main(int argc, const char **argv){
    if(argc != 3) goto error;

    if(!strcmp(argv[1], "compile")){
        std::cerr << argv[2] << std::endl;
        if(_compile(argv[2]) != 0){
            std::cerr << "compile failed" << std::endl;
            goto error;
        }
    }

    return 0;

  error:
    std::cerr << "Error" << std::endl;
    return -1;
}
