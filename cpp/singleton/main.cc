#include <iostream>

#include "optimization.h"

int main(const int argc, const char **argv){
    std::string search;
    if(argc < 2){
        std::cerr << "Please input domain." << std::endl;
        return -1;
    }
    search = argv[1];

    std::cout << "OK: " << search << std::endl;

    Optimization *opt  = Optimization::GetInstance();
    Optimization *opt2 = Optimization::GetInstance();

    if(opt->IsLowPerformanceDomain(search)){
        std::cout << "True: " << search << std::endl;
    }
    else {
        std::cout << "False: " << search << std::endl;
    }

    if(opt2->IsLowPerformanceDomain(search)){
        std::cout << "True: " << search << std::endl;
    }
    else {
        std::cout << "False: " << search << std::endl;
    }

    return 0;
}
