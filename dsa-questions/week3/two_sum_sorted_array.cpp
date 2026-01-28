// Two Sum in Sorted Array
#include <iostream>
#include <vector>
using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
    int left = 0, right = nums.size() - 1;

    while (left < right) {
        int sum = nums[left] + nums[right];

        if (sum == target)
            return {left, right};
        else if (sum < target)
            left++;
        else
            right--;
    }
    return {};
}

int main() {
    vector<int> nums = {1,2,3,4,5,6,7,8,9,10};
    int target;
    cout<<"enter the target :";
    cin>>target;

    vector<int> res = twoSum(nums, target);
    cout << "sum of index:"<<res[0] << " and " << res[1]<<" is equal to target:" <<target<< endl;

    return 0;
}
