#include <iostream>
#include <unordered_map>
using namespace std;

int countDuplicates(int arr[], int n) {
    unordered_map<int, int> freq;
    int duplicates = 0;

    for (int i = 0; i < n; i++) {
        freq[arr[i]]++;
    }

    for (auto it : freq) {
        if (it.second > 1)
            duplicates += it.second - 1;
    }

    return duplicates;
}

int main() {
    int arr[] = {1, 2,1,3,4,5,6,7,8,8,7,6,5, 3, 2, 1};
    int n =16;

    cout << countDuplicates(arr, n);
    return 0;
}
