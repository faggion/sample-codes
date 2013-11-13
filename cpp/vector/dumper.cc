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

#include <fstream>
#include <sstream>
#include <iostream>
#include <vector>
#include <string>
#include <map>

// http://stackoverflow.com/questions/11303702/converting-from-stdvector-to-a-double-pointer
int main()
{
    std::vector<int> array;
    int *ele;

    array.push_back(10);
    array.push_back(20);
    array.push_back(30);

    for(unsigned int i=0;i<array.size();i++){
        std::cerr << "array val1 = " << array[i] << std::endl;
    }

    ele = array.data();
    for(unsigned int i=0;i<array.size();i++){
        std::cerr << "array val2 = " << ele[i] << std::endl;
    }

    ele = &array[0];
    for(unsigned int i=0;i<array.size();i++){
        std::cerr << "array val3 = " << ele[i] << std::endl;
    }

    return EXIT_SUCCESS;
}

