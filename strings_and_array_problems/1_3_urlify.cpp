#include <string>
#include <iostream>

using namespace std;

int main()
{
    string str = "Mr John Smith   ", new_string;
    string placeholder = "%20";
    int len = 13;

    for(int i = 0; i < len; i++){
        if(str[i] == ' ')
            new_string += placeholder;
        else
            new_string += str[i];
    }
    cout << new_string << endl;

    return 0;
}