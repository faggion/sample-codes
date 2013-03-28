#include <stdio.h>
#include <string.h>

#include "lua.h"
#include "lualib.h"
#include "lauxlib.h"

int main (void)
{
    //char code1[] = "a = 5; return 3;";
    char code1[] = "return (function() local a = 5; return 3;end)()";
    //char code2[] = "return a;";
    int ret, rc, nret, top;

    // Luaを開く
    lua_State* L = luaL_newstate();
    // Luaの標準関数を使用できる状態にする
    luaL_openlibs(L);
    // メモリからluaコードを読み込む
    top = lua_gettop(L);
    ret = luaL_loadbuffer(L, code1, strlen(code1), "buffer1");
    if( ret != 0 ) {
        printf("error : %s\n", lua_tostring(L, -1) );
        // 失敗してもスタックにはつまれてるのでpopする
        lua_pop(L,1);
        return 1;
    }

    /* 処理 start */
    ret = lua_pcall(L, 0, LUA_MULTRET, 0);
    if( ret != 0 ) {
        printf("error : %s\n", lua_tostring(L, -1) );
        lua_pop(L,1);
        return 1;
    }

    nret = lua_gettop(L) - top;
    if( nret > 0 ){
        switch( lua_type(L,-1) ){
        case LUA_TBOOLEAN:
            rc = lua_toboolean(L,-1);
            break;
        case LUA_TNUMBER:
            rc = lua_tointeger(L,-1);
            break;
        default:
            break;
        }

        lua_pop(L,nret);
    }
    //rc = lua_tointeger(L,-1);
    printf("Return: %d\n", rc);
    /* 処理 end */
    return 0;
}
