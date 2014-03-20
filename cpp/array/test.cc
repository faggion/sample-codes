#include <iostream>
#include <string>
#include <map>

#define ARRAY_LEN(array) (sizeof(array) / sizeof(array[0]))
const std::string names[] = {
    "goo",
    "choki",
    "par",
};

int main(const int argc, const char **argv){
    std::string name = "foo";
    std::cout << "hello, " << name << std::endl;
    std::cout << "hello, " << name[0] << std::endl;

    std::cout << "names length = " << ARRAY_LEN(names) << std::endl;
    return 0;
}
