#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

#include "json/json.h"

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

    struct json_object *obj = json_object_from_file(configfile);

    // 入力ファイルエラー
    if(is_error(obj)){
        fprintf(stderr, "read json file error: %s\n", configfile);
        return usage(argc, argv);
    }

    printf("parse and stringfy: %s\n", json_object_to_json_string(obj));
    json_object_put(obj);

    return 0;
}
