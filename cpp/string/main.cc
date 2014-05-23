#include <iostream>

bool getJSON(std::string &buf, int is_empty){
    if(is_empty){
        buf.clear();
        return false;
    }
    buf = "xxx";
    return true;
}

int main(void){
    std::string ret;
    std::string foo = "";
    std::string bar = "aaa";

    if(foo.empty()){
        std::cout << "True" << std::endl;
    }
    else {
        std::cout << "False" << std::endl;
    }

    if(getJSON(ret, 1) || getJSON(ret, 0)){
        std::cout << "ret = " << ret << std::endl;
    }

    if(getJSON(ret, 1)){
        std::cout << "SHOULD NOT OUTPUT THIS MESSAGE." << std::endl;
    }

    if(getJSON(ret, 0)){
        std::cout << "OK." << std::endl;
    }

    return 0;
}
