#include <bits/stdc++.h>
using namespace std;

class Solution {
    void buildMaxHeap(vector<int>& nums) {
        int n = nums.size();
        for (int i = (n - 1) / 2; i >= 0; --i) {
            maxHeapify(nums, i, n);
        }
    }

    void maxHeapify(vector<int>& nums, int i, int n) {
        while (i * 2 + 1 < n) {
            // 代表当前 i 节点的左右儿子；
            // 超出数组大小则代表当前 i 节点为叶子节点，不需要移位
            int lSon = 2 * i + 1;
            int rSon = 2 * i + 2;
            int large = i;
            if (lSon < n && nums[lSon] > nums[i]) large = lSon;
            if (rSon < n && nums[rSon] > nums[large]) large = rSon;

            if (large != i) {
                swap(nums[i], nums[large]);
                // 迭代判断对应子节点及其儿子节点的大小关系
                i = large;
            } else {
                break;
            }
        }
    }

public:
    vector<int> sortArray(vector<int>& nums) {
        // heapSort 堆排序
        int n = nums.size();
        // 将数组整理成大根堆
        buildMaxHeap(nums);
        for (int i = n - 1; i >= 1; --i) {
            // 依次弹出最大元素，放到数组最后，当前排序对应数组大小 - 1
            swap(nums[0], nums[i]);
            --n;
            maxHeapify(nums, 0, n);
        }
        return nums;
    }
};