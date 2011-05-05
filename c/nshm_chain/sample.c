#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <nshm.h>
#include <sys/types.h>

#define PATH            "/tmp/items.nshm"
#define SIZE            1024*1024
#define TABLE_NAME      "items"
//#define TABLE_NAME_SIZ  5
#define ITEM_BUCKET_SIZ 1024
#define SELLER_NUM      32
#define BUF_SIZ  128

/*
 * 1 商品ID   -> 1 sellerID ( seller:item = 1:N )
 * 商品IDからseller情報を検索するのが目的
 */

/*
 * 商品情報
 */
typedef struct {
    int64_t id;
    int64_t price;
    int64_t name_offset;
    int64_t seller_offset;
} Item;

/*
 * 販売者情報
 */
typedef struct {
    int64_t id;
    int64_t name_offset;
} Seller;

int init(){
    NShm    *n;
    Item    *item;
    Seller  *seller;
    int64_t *sellers;
    int64_t *items;
    int32_t ret=0, ix;
    char    buf[BUF_SIZ];
    char    *seller_name, *item_name;

    n = nshm_create(PATH, SIZE, 0666);
    DEF_NSHMBASE(n);

    // table領域を確保
    items   = (int64_t *)nshm_memalloc(n, sizeof(int64_t)*ITEM_BUCKET_SIZ);
    sellers = (int64_t *)nshm_memalloc(n, sizeof(int64_t)*SELLER_NUM);
    // tableを初期化
    for(ix=0; ix<ITEM_BUCKET_SIZ;ix++){
        items[ix] = -1;
    }
    for(ix=0; ix<SELLER_NUM;ix++){
        sellers[ix] = -1;
    }

    // sellerを追加
    for(ix=0;ix<SELLER_NUM;ix++){
        memset(buf, 0, BUF_SIZ);
        sprintf(buf, "seller-%d", ix);

        seller      = (Seller *)nshm_memalloc(n, sizeof(Seller));
        seller_name = (char *)nshm_memalloc(n, (int32_t)(strlen(buf)+1));
        strcpy(seller_name, (const char *)buf);

        seller->id = ix;
        seller->name_offset = vos_assign(int64_t, seller_name);
        sellers[ix] = vos_assign(int64_t, seller);
    }

    // itemを追加
    for(ix=0;ix<ITEM_BUCKET_SIZ;ix++){
        memset(buf, 0, BUF_SIZ); 
        sprintf(buf, "item-%d", ix);
        item      = (Item *)nshm_memalloc(n, sizeof(Item));
        item_name = (char *)nshm_memalloc(n, (int32_t)(strlen(buf)+1));
        strcpy(item_name, (const char *)buf);

        item->id            = ix;
        item->price         = 1000 + ix;
        item->name_offset   = vos_assign(int64_t, item_name);
        item->seller_offset = sellers[ix % SELLER_NUM];
        items[ix] = vos_assign(int64_t, item);
    }

    // Tableを保存
    ret = nshm_set(n, TABLE_NAME, (int)strlen(TABLE_NAME), (const void *)items);
    nshm_detach(n);

    return ret;
}

int lookup(int64_t id){
    void *_nshm_base=NULL;
    int64_t *items;
    Item    *item;
    Seller  *seller;
    NShm    *n;
    char    *item_name, *seller_name;

    n  = nshm_attach(PATH);
    items = (int64_t *)nshm_get(n, TABLE_NAME, (int)strlen(TABLE_NAME));
    SET_NSHMBASE(n);

    fprintf(stderr, "item id[%ld]\n", (long)id);
    item = vos_ptr(Item *, items[id]);
    fprintf(stderr, "item price[%ld]\n", (long)item->price);
    item_name = vos_ptr(char *, item->name_offset);
    fprintf(stderr, "item name[%s]\n", item_name);

    seller = vos_ptr(Seller *, item->seller_offset);
    fprintf(stderr, "seller id[%ld]\n", (long)seller->id);
    seller_name = vos_ptr(char *, seller->name_offset);
    fprintf(stderr, "seller name[%s]\n", seller_name);

    nshm_detach(n);
    return 0;
}

int main(int argc, const char **argv){
    int ix;

    if(argc < 2){
        goto error;
    }

    if(!strcmp(argv[1], "init")){
        init();
        return 0;
    }
    else if(2 < argc &&
            !strcmp(argv[1], "lookup")){
        lookup((int64_t)atoi(argv[2]));
        return 0;
    }
    else if(!strcmp(argv[1], "bench")){
        for(ix=0;ix<100000;ix++){
            lookup((int64_t)(ix % ITEM_BUCKET_SIZ));
        }
        return 0;
    }
    goto error;

  error:
    fprintf(stderr, "error\n");
    return -1;
}
