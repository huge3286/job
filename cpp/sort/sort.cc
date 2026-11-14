#include "sort.h"

#include <utility>

void quickSort(std::vector<int>& nums, int begin, int end) {
    while (begin < end) {
        const int pivot = nums[begin + (end - begin) / 2];
        int lower = begin;
        int current = begin;
        int upper = end;
        while (current <= upper) {
            if (nums[current] < pivot) {
                std::swap(nums[lower++], nums[current++]);
            } else if (nums[current] > pivot) {
                std::swap(nums[current], nums[upper--]);
            } else {
                ++current;
            }
        }

        // 递归处理较短的一边，栈深度最多为 O(log n)。
        if (lower - begin < end - upper) {
            quickSort(nums, begin, lower - 1);
            begin = upper + 1;
        } else {
            quickSort(nums, upper + 1, end);
            end = lower - 1;
        }
    }
}
