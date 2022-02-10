#include <iostream>

using namespace std;

class MyClass {
    
    public:
        int Num = 6;
        string String = "Hello World";
        double Double = 6.50;
        char Char = '*';

};

int main () {
    
    MyClass Obj;
    cout << Obj.Num << endl;
    cout << Obj.String << endl;
    cout << Obj.Double << endl;
    cout << Obj.Char << endl;
    return 0;

}