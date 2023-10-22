#include <iostream>
#include "sort.h"


void quickSort(std::vector<int>& nums, int begin, int end) {
    // 递归出口
    if (begin >= end) return;

    // 随机pivot
    int pivot = begin + std::rand() % (end - begin + 1);
    std::swap(nums[pivot], nums[begin]);

    // 排序
    int i = begin, j = end;
    while (i < j) {
        while (i < j and nums[j] >= nums[begin]) j--;
        while (i < j and nums[i] <= nums[begin]) i++;
        std::swap(nums[i], nums[j]);
    }
    std::swap(nums[i], nums[begin]);

    // 去重
    while (i > begin and nums[i] == nums[i-1]) i--;
    while (j < end and nums[j] == nums[j+1]) j++;

    // 继续递归
    quickSort(nums, begin, i - 1);
    quickSort(nums, j + 1, end);
}



template <typename T>
void print(const T& x) {
    for (const auto& i : x) {
        std::cout << i << ' ';
    }
    std::cout << std::endl;
}


