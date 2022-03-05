//Author: Zach Naymik
//Date: March 5, 2022

#include <iostream>
#include <iomanip>
#include <cstdlib>

using namespace std;

int* buildArray(int nums[]);

int main() {
    int nums[6] = {0,2,1,5,3,4};
    cout << buildArray(nums);
}

int* buildArray(int nums[]) {
    int* new_array = nums;
    int new_index;
    for (int i = 0; i < (sizeof(nums) / sizeof(nums[0])); i++) {
        new_index = nums[nums[i]];
        new_array[new_index] = nums[new_index];
    }
    return new_array;
}