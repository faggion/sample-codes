#include <iostream>
#include <cassert>
#include <stdio.h>
#include <stdlib.h>

int main (int argc, char** argv)
{
    int ret;
    char* p;

    //ret = posix_memalign((void**)&p, 128, 16*1024);
    ret = posix_memalign((void**)&p, 128, 128);
    assert (ret == 0);

    std::cout << "p = " << (void*)p << "\n";

    free(p);
    return 0;
}
