#include <bits/stdc++.h>
using namespace std;

class Solution {
    vector<int> tmp;
    void mergeSort (vector<int>& nums, int l, int r) {
        if (l >= r) return; // 不需进行排列
        int mid = l + (r - l) / 2;
        // 自底向上
        mergeSort(nums, l, mid);
        mergeSort(nums, mid + 1, r);
        // 排序当前数组
        int i = l, j = mid + 1, pos = l;
        while (i <= mid && j <= r) {
            if (nums[i] <= nums[j]) {
                tmp[pos] = nums[i];
                ++i;
            } else {
                tmp[pos] = nums[j];
                ++j;
            }
            ++pos;
        }
        for (int k = i; k <= mid; ++k) {
            tmp[pos++] = nums[k];
        }
        for (int k = j; k <= r; ++k) {
            tmp[pos++] = nums[k];
        }
        copy(tmp.begin() + l, tmp.begin() + r + 1, nums.begin() + l);
    }
public:
    vector<int> sortArray(vector<int>& nums) {
        int n = nums.size();
        tmp = nums;
        mergeSort(nums, 0, n - 1);
        return nums;
    }
};