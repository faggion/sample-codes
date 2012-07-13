#include <stdio.h>

#include "lua.h"
#include "lualib.h"
#include "lauxlib.h"

int main (void)
{
    //Luaを開く
    lua_State* L = luaL_newstate();
    //Luaの標準関数を使用できる状態にする
    luaL_openlibs(L);
    //Luaファイルsample.luaを読み込む
    if( luaL_loadfile(L, "sample.lua") || lua_pcall(L, 0, 0, 0) ) {
        printf("sample.luaを開けませんでした\n");
        printf("error : %s\n", lua_tostring(L, -1) );
        return 1;
    }

    /* 処理 start */
    //PATHを取得しスタックに積む
    lua_getglobal(L, "NAME");
    //SIZEを取得しスタックに積む
    lua_getglobal(L, "SIZE");
        
    if( !lua_isstring(L, -2) || !lua_isnumber(L, -1) ) {
        printf("正しく値が取得できませんでした\n");
        return 1;
    }
    // FIXME: スタックから値をpopしておくべき
    printf("NAME : %s\n", lua_tostring(L, -2));
    printf("SIZE : %d\n", (int)lua_tointeger(L, -1));
    /* 処理 end */

    lua_close(L);
    return 0;
}
