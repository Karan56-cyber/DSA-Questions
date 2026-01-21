/*
Problem Name: Find i, j, k such that arr[i] + arr[j] = arr[k]

Problem Statement:
Given an array of integers, determine whether there exist
three indices i, j, and k such that:
arr[i] + arr[j] = arr[k] where i < j < k.

Input:
- n (number of elements)
- n integers

Output:
- Print the values arr[i], arr[j], and arr[k] if such a triplet exists
- Otherwise, print "No such triplet exists"

Approach:
- Sort the array
- Fix k from the last index to index 2
- Use two pointers i and j to check if arr[i] + arr[j] = arr[k]

Time Complexity: O(n^2)
Space Complexity: O(1)
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void twoSumTriplet(vector<int>& arr) {
    int n = arr.size();

    sort(arr.begin(), arr.end());  // REQUIRED

    for (int k = n - 1; k >= 2; k--) {
        int i = 0;
        int j = k - 1;

        while (i < j) {
            int sum = arr[i] + arr[j];

            if (sum == arr[k]) {
                cout << "Triplet found: "
                     << arr[i] << " + " << arr[j]
                     << " = " << arr[k];
                return;
            }
            else if (sum < arr[k]) {
                i++;
            }
            else {
                j--;
            }
        }
    }

    cout << "No such triplet exists";
}

int main() {
    int n, ele;
    vector<int> arr;

    cout << "Enter number of elements: ";
    cin >> n;

    cout << "Enter elements:\n";
    for (int i = 0; i < n; i++) {
        cin >> ele;
        arr.push_back(ele);
    }

    twoSumTriplet(arr);

    return 0;
}
