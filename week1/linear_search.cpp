/*
Problem Name: Linear Search

Problem Statement:
Given an array of integers and an element to be searched,
find the index of the element using Linear Search.
If the element is not present, return -1.

Input:
- First line: number of elements (n)
- Second line: n integers (array elements)
- Third line: element to be searched

Output:
- Index of the element if found
- Otherwise, print "element not found in array"

Approach:
- Traverse the array from index 0 to n-1
- Compare each element with the target element
- If match found, return the index
- If traversal ends, return -1

Time Complexity: O(n)
Space Complexity: O(1)
*/

#include <iostream>
#include <vector>
using namespace std;

int linearSearch(const vector<int>& arr, int ele) {
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] == ele) {
            return i;
        }
    }
    return -1;
}

int main() {
    int n, ele;
    vector<int> arr;

    cout << "Enter the number of elements in the array: ";
    cin >> n;

    cout << "Enter the elements:\n";
    for (int i = 0; i < n; i++) {
        cin >> ele;
        arr.push_back(ele);
    }

    cout << "Enter the element to be searched: ";
    cin >> ele;

    int index = linearSearch(arr, ele);

    if (index == -1) {
        cout << "Element not found in array";
    } else {
        cout << "Element found at index: " << index;
    }

    return 0;
}
