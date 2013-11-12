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

#include <rapidjson/document.h>

int main(const int argc, const char **argv)
{
    rapidjson::Document doc;
    std::ifstream ifs(argv[1]);
    std::stringstream ss;
    ss << ifs.rdbuf();
    std::string jsonstr = ss.str();

    //std::cerr << jsonstr << std::endl;

    if (doc.Parse<0>(jsonstr.c_str()).HasParseError()) {
        std::cerr << "parse error" << std::endl;
        return 1;
    }

    rapidjson::Value& schedules = doc["schedules"];

    if(schedules.IsArray()){
        std::cerr << "schedules = array" << std::endl;
    }

    for(rapidjson::SizeType i = 0; i < schedules.Size(); i++){
        std::cerr << schedules[i].GetInt() << std::endl;
    }

    return EXIT_SUCCESS;
}

