#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <string>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int main() {

int nums[] = {1,2,3,4};
int runningSum[sizeof(nums)/sizeof(nums[0])] = { };
int total = 0;

for (unsigned int i = 0; i < sizeof(nums)/sizeof(nums[0]); i++) {
    total += nums[i];
    runningSum[i] = total;
}

cout << runningSum << endl;

} //main

