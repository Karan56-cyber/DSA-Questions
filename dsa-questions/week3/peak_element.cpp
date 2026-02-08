// Peak Element
#include <iostream>
#include <vector>
using namespace std;

int findPeakElement(vector<int>& nums) {
    int low = 0, high = nums.size() - 1;

    while (low <= high) {
        int mid = low + (high - low) / 2;

        if ((nums[mid] >= nums[mid - 1]) &&
            ( nums[mid] >= nums[mid + 1])) {
            return mid;
        }
        else if (nums[mid] < nums[mid + 1]) {
            low = mid + 1;
        }
        else {
            high = mid - 1;
        }
    }
    return -1;
}

int main() {
    vector<int> nums = {1, 2, 3, 1};

    int idx = findPeakElement(nums);
    
    cout << "peak element:"<<nums[idx] << endl;

    return 0;
}
