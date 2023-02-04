#include <iostream>

#include<ctime>

#include<random>

using namespace std;

int length = 0;

void input(int* arr) {

for (int i = 0; i < length; i++) {

cin >> arr[i];

}

}

void output(int* arr) {

for (int i = 0; i < length; i++) {

cout << arr[i] << " ";

}

}

void SelectionSort(int* arr) {

for (int i = 0; i < length-1; i++) {

int minindex = i;

for (int j = i + 1; j < length; j++) {

if (arr[minindex] > arr[j]) {

minindex = j;

}

}

int buf = arr[i];

arr[i] = arr[minindex];

arr[minindex] = buf;

}

}

int main() {

int size;

cin >> size;

length = size;

int* arr = new int[size];

input(arr);

SelectionSort(arr);

output(arr);

return 0;