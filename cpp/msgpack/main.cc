#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

#include <msgpack.hpp>

int main(void) {
    std::ifstream ifs("/tmp/data.bin");
    std::stringstream buffer;
    buffer << ifs.rdbuf();
    std::string result = buffer.str();
    //std::cout << result;
    
    std::cout << "bin size: " << result.size() << std::endl;
    
    msgpack::unpacked msg;
    msgpack::unpack(&msg, result.data(), result.size());
    msgpack::object obj = msg.get();
    
    std::cout << obj << std::endl;

    return 0;
}
