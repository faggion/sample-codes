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
    int x = 10, y = 5;

    //add関数をスタックに積む
    lua_getglobal(L, "add");
    //第1引数x
    lua_pushnumber(L, (float)x);
    //第2引数y
    lua_pushnumber(L, (float)y);

    //add(x, y)を呼び出す 引数2個，戻り値1個
    if(lua_pcall(L, 2, 1, 0) != 0) {
        printf("関数呼び出し失敗\n");
        printf("error : %s\n", lua_tostring(L, -1) );
        return 1;
    }
    if( lua_isnumber(L, -1) ) {
        printf("結果 : %d\n", (int)lua_tointeger(L, -1) );
        lua_pop(L,1); //戻り値をポップ
    }
    /* 処理 end */

    lua_close(L);
    return 0;
}
