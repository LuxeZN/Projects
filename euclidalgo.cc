#include <iostream>
#include <iomanip>
#include <vector>
#include <cstdlib>
#include <algorithm>

using namespace std;

int EuclidAlgorithm(int first, int second);

int main() {
    cout << EuclidAlgorithm(135, 144) << endl;
}

int EuclidAlgorithm(int first, int second) {
    if (first % second == 0) {return second;}
    else {
        return EuclidAlgorithm(second, (first % second));
    }
}