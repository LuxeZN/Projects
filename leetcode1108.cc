//Author: Zach Naymik
//Date: March 5, 2022

#include <iostream>
#include <iomanip>
#include <string>
#include <cstdlib>
#include <cctype>

using namespace std;

string defangIPAddress(string address);

int main() {
     string address = "1.1.1.1";
     cout << defangIPAddress(address);
}

string defangIPAddress(string address) {
    string new_string;
    for (unsigned int i = 0; i < address.length(); i++) {
        if (address[i] == '.') {
            new_string += "[.]";
        }
        else {
            new_string += address[i];
        }
    }
    return new_string;
}

