#include <iostream>
#include <iomanip>
#include <cstdlib>

using namespace std;

int main() {

    int a[] = {1, 1, 1};
    int b[] = {1, 1, 1};
    int c[] = {1, 1, 1};
    int* matrix[] = {a, b, c};

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }

    cout << endl;

    int d[] = {2, 2, 2};
    int e[] = {2, 2, 2};
    int f[] = {2, 2, 2};
    int* matrix2[] = {d, e, f};

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cout << matrix2[i][j] << " ";
        }
        cout << endl;
    }

    cout << endl;

    int g[] = {0, 0, 0};
    int h[] = {0, 0, 0};
    int i[] = {0, 0, 0};
    int* matrix_result[] = {g, h, i};
    int total = 0, result;
    
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            for (int k = 0; k < 3; k++) {
                result = (matrix[i][j] * matrix2[j][i]);
                matrix_result[i][j] += result;
            } 
        }
    }

for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cout << matrix_result[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}