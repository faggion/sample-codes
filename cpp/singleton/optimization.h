#include <string>
#include <map>

class Optimization {
  public:
    static Optimization* GetInstance(){
        static Optimization instance;
        return &instance;
    }
    bool IsLowPerformanceDomain(std::string domain_name);
    
  private:
    std::map<std::string, int> _lowPerformanceDomains;

    Optimization();
    Optimization(const Optimization& rhs);
    Optimization& operator=(const Optimization& rhs);
};
