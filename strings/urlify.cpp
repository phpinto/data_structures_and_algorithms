#include <iostream>
#include <string>

using namespace std;

void urlify(string &url) {
    bool inURL = false;
    int shift = 0;
    int i = url.length() - 1;

    while (i >= 0) {
        if (!inURL) {
            if (url[i] != ' ') {
                inURL = true;
            } 
            else {
                shift++;
                i--;
                continue;
            }
        }
        else {
            if (url[i] == ' ') {
                url[shift + i] = '0';
                url[shift + i - 1] = '2';
                url[shift + i - 2] = '%';
                i--;
                shift -= 2;
                continue;
            }
        }
        url[i + shift] = url[i];
        i--;
    }
}

int main() {
    string url = "Mr John Smith    ";
    cout << url << endl;
    urlify(url);
    cout << url << endl;
}