#include <iostream>
#include "optimization.h"

Optimization::Optimization(){
    _lowPerformanceDomains["yahoo.co.jp"] = 1;
    _lowPerformanceDomains["yahoo.com"] = 1;
    _lowPerformanceDomains["yahoo.jp"] = 1;
}

bool Optimization::IsLowPerformanceDomain(std::string domain_name){
    std::map<std::string, int>::iterator it;
    it = _lowPerformanceDomains.find(domain_name);
    if(it == _lowPerformanceDomains.end()){
        return false;
    }
    return true;
}
