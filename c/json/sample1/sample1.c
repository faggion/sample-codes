#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

#include "json/json.h"
#include "json/json_object.h"

#define MAX_FILE_PATH 1024

int usage(int argc, char *argv[]){
    if(0 < argc){
        fprintf(stderr, "Usage %s:\n", argv[0]);
        fprintf(stderr, "    -f config file path\n");
    }
    return -1;
}

int main(int argc, char *argv[]){
    int ch;
    extern char *optarg;
    extern int  optind, opterr;
    char configfile[MAX_FILE_PATH+1] = {0};
    struct json_object *hash, *obj, *arr, *arr_ele;

    while ((ch = getopt(argc, argv, "f:")) != -1){
        switch (ch){
        case 'f':
            snprintf(configfile, MAX_FILE_PATH, "%s", optarg);
            break;
        default:
            return usage(argc, argv);
        }
    }

    // 入力ファイル指定無し
    if((int)strlen(configfile) < 1){
        return usage(argc, argv);
    }

    obj = json_object_from_file(configfile);

    // 入力ファイルエラー
    if(is_error(obj)){
        fprintf(stderr, "read json file error: %s\n", configfile);
        return usage(argc, argv);
    }

    printf("parse and stringfy: %s\n", json_object_to_json_string(obj));

    printf("get 'nokey' key value: %s\n", json_object_get_string(json_object_object_get(obj, "hoge")));
    printf("get 'nokey' key value: %s\n", json_object_get_string(json_object_object_get(obj, "nokey")));

    hash = json_object_object_get(obj, "hash");
    // -std=gnu99オプションが必要
    json_object_object_foreach(hash, key, val){
        fprintf(stderr, "%s = %s\n", key, json_object_get_string(val));
    }
    //json_object_put(hash); --> jsonの一部分なのでfreeいらない

    arr = json_object_object_get(obj, "array");
    int len = json_object_array_length(arr);
    printf("array length: %d\n", len);
    for(int i=0;i<len;i++){
        arr_ele = json_object_array_get_idx(arr, i);
        fprintf(stderr, "element %d = %s\n", i, json_object_get_string(arr_ele));
        //json_object_put(arr_ele); --> jsonの一部分なのでfreeいらない
    }
    //json_object_put(arr); --> jsonの一部分なのでfreeいらない

    // 開放
    json_object_put(obj); // --> json全体のfree

    return 0;
}
