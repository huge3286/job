#include <algorithm>
#include <vector>

#include <gtest/gtest.h>

#include "sort.h"

TEST(QuickSort, MatchesStandardSort) {
    for (auto input : std::vector<std::vector<int>>{
             {}, {7}, {5, 2, 9, 1, 5, 6}, {1, 2, 3, 4},
             {4, 3, 2, 1}, {0, -2, 5, -2}, std::vector<int>(10000, 7)}) {
        auto expected = input;
        std::sort(expected.begin(), expected.end());
        quickSort(input, 0, static_cast<int>(input.size()) - 1);
        EXPECT_EQ(input, expected);
    }
}

TEST(QuickSort, SortsOnlyTheRequestedRange) {
    std::vector<int> input{9, 4, 3, 1, 8};
    quickSort(input, 1, 3);
    EXPECT_EQ(input, (std::vector<int>{9, 1, 3, 4, 8}));
}
