#include <stdio.h>
#include <string.h>
//#define CRC32_POLY 0x82F63B78 // CRC-32C (Castagnoli)
#define CRC32_POLY 0xEDB88320 // CRC-32-IEEE 802.3

unsigned int crc_table[256], crc_table_init=0;

void make_crc_table(){
    unsigned int i, j, x;
    for (i = 0; i < 256; i++){
        x = i;
        for (j = 8; j > 0; j--) {
            if (x&1) x= (x>>1) ^ CRC32_POLY;
            else x>>= 1;
        }
        crc_table[i]=x;
    }
}

unsigned int crc32 (unsigned char *p, unsigned int length){
    unsigned int i, x = 0xFFFFFFFF;
    if(!crc_table_init) make_crc_table();
    for (i = 0; i < length; i++)
        x = ((x >> 8) & 0x00FFFFFF) ^ crc_table[(x ^ p[i]) & 0xFF];
    return x ^ 0xFFFFFFFF;
}

int main(int argc, char **argv){
    printf("%u\n", crc32((unsigned char *)argv[1], (unsigned int)strlen(argv[1])));
}
