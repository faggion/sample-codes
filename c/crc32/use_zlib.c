#include <stdio.h>
#include <string.h>
#include <zlib.h>

int main(const int argc, const char **argv){
    unsigned long a = crc32(0L, Z_NULL, 0);
    fprintf(stderr, "OK: %ld\n", a);
    //fprintf(stderr, "OK: %ld\n", crc32(a, argv[1], strlen(argv[1]))); 
    fprintf(stderr, "OK: %ld\n", crc32(0, argv[1], strlen(argv[1])));
    return 0;
}
