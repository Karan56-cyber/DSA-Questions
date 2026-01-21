/*
Problem Name: Count Occurrences in a Sorted Array

Problem Statement:
Given a sorted array and a number x, find the number of
occurrences of x in the array.

Input:
- n (size of array)
- n sorted integers
- element x

Output:
- Number of occurrences of x

Approach:
- Use binary search to find first occurrence
- Use binary search to find last occurrence
- Count = last - first + 1

Time Complexity: O(log n)
Space Complexity: O(1)
*/

#include <iostream>
#include <vector>
using namespace std;

int firstOccurrence(const vector<int>& arr, int x) {
    int low = 0, high = arr.size() - 1, ans = -1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == x) {
            ans = mid;
            high = mid - 1;
        } else if (arr[mid] < x) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return ans;
}

int lastOccurrence(const vector<int>& arr, int x) {
    int low = 0, high = arr.size() - 1, ans = -1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == x) {
            ans = mid;
            low = mid + 1;
        } else if (arr[mid] < x) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return ans;
}

int main() {
    int n, x;
    vector<int> arr;

    cout << "Enter number of elements: ";
    cin >> n;

    cout << "Enter sorted elements:\n";
    for (int i = 0; i < n; i++) {
        int ele;
        cin >> ele;
        arr.push_back(ele);
    }

    cout << "Enter element to count: ";
    cin >> x;

    int first = firstOccurrence(arr, x);
    int last = lastOccurrence(arr, x);

    if (first == -1) {
        cout << "Element not found";
    } else {
        cout << "Number of occurrences: " << (last - first + 1);
    }

    return 0;
}
