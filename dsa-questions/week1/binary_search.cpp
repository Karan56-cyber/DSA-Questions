/*
Problem Name: Binary Search

Problem Statement:
Given a list of integers sorted in ascending order and a target element,
find the index of the target element using Binary Search.
If the element is not present, return -1.

Input:
- First line: number of elements (n)
- Second line: n integers (array elements)
- Third line: element to be searched

Output:
- Index of the element if found
- Otherwise, print "element not found in array"

Approach:
- Sort the array (to ensure binary search works correctly)
- Use two pointers (low and high)
- Find mid element
- Reduce search space based on comparison

Time Complexity:
- Sorting: O(n log n)
- Binary Search: O(log n)

Space Complexity: O(1)
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int binarySearch(const vector<int>& arr, int ele) {
    int low = 0, high = arr.size() - 1;

    while (low <= high) {
        int mid = low + (high - low) / 2;

        if (arr[mid] == ele)
            return mid;
        else if (arr[mid] < ele)
            low = mid + 1;
        else
            high = mid - 1;
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

    int index = binarySearch(arr, ele);

    if (index == -1) {
        cout << "Element not found in array";
    } else {
        cout << "Element found at index: " << index;
    }

    return 0;
}
