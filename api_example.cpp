#include <iostream>
#include <curl/curl.h>
#include <string>

using namespace std;

size_t WriteCallback(void* contents, size_t size, size_t nmemb, string* output) {
    size_t totalSize = size * nmemb;
    output->append((char*)contents, totalSize);
    return totalSize;
}

int main() {
    CURL* curl;
    CURLcode res;
    string readBuffer;

    string api_key = "fb73ef7efbe026084ed9f2ec03f1c9e7"; // Replace this!
    string city = "London";
    string url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key;

    curl_global_init(CURL_GLOBAL_DEFAULT);
    curl = curl_easy_init();

    if (curl) {
        curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &readBuffer);
        res = curl_easy_perform(curl);
        curl_easy_cleanup(curl);
    }

    curl_global_cleanup();

    cout << "API Result:\n" << readBuffer << endl;
    return 0;
}
