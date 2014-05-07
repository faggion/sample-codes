// clang++ -I/usr/include -lcurl parse_remote_json.cc && ./a.out

#include <string>
#include <iostream>
#include <curl/curl.h>

#include "rapidjson/document.h"

using namespace std;

size_t callbackWrite(char *ptr, size_t size, size_t nmemb, string *stream)
{
    int dataLength = size * nmemb;
    stream->append(ptr, dataLength);
    return dataLength;
}

int main()
{
    CURL *curl;
    CURLcode ret;

    curl = curl_easy_init();
    string chunk;

    if (curl == NULL) {
        cerr << "curl_easy_init() failed" << endl;
        return 1;
    }

    // Open Weather Map: http://openweathermap.org/API
    curl_easy_setopt(curl, CURLOPT_URL, "http://api.openweathermap.org/data/2.5/weather?q=Tokyo,jp");
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, callbackWrite);
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, &chunk);
    ret = curl_easy_perform(curl);
    curl_easy_cleanup(curl);

    if (ret != CURLE_OK) {
        cerr << "curl_easy_perform() failed." << endl;
        return 1;
    }

    cout << chunk << endl;

    rapidjson::Document doc;
    if(doc.Parse<0>(chunk.c_str()).HasParseError()){
        cerr << "parse error" << endl;
        return 1;
    }
    cout << "------" << endl;

    rapidjson::Value& ele = doc["id"];
    cout << "id: type=" << ele.GetType() << ", IsNull=" << ele.IsNull() << ", doc.HasMember=" << doc.HasMember("id") << ", value=" << ele.GetInt() << endl;

    ele = doc["base"];
    cout << "base: type=" << ele.GetType() << ", IsNull=" << ele.IsNull() << ", doc.HasMember=" << doc.HasMember("base") << ", value=" << ele.GetString() << endl;

    if(doc["main"].IsObject()){
        ele = doc["main"];
        if(ele["temp"].IsDouble()) cout << "  temp: type=" << ele["temp"].GetType() << ", IsNull=" << ele["temp"].IsNull() << ", value=" << ele["temp"].GetDouble() << endl;
        if(ele["humidity"].IsInt()) cout << "  humidity: type=" << ele["humidity"].GetType() << ", IsNull=" << ele["humidity"].IsNull() << ", value=" << ele["humidity"].GetInt() << endl;
    }

    ele = doc["weather"];
    if(ele.IsArray()){
        int i, l = ele.Size();
        cout << "weather element size = " << l;
        if(l){
            cout << ", weather[0][id]=" << ele[rapidjson::SizeType(0)]["id"].GetInt() << ", weather[0][description]=" << ele[rapidjson::SizeType(0)]["description"].GetString() << endl;
        }
    }

    return 0;
}
