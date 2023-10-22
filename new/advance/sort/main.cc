#include <vector>
#include <gtest/gtest.h>
#include "sort.h"

TEST(sort, exp1) {
    std::vector<int> input = {5, 2, 9, 1, 5, 6};
    std::vector<int> expected = {1, 2, 5, 5, 6, 9};

    quickSort(input, 0, input.size() - 1);

    EXPECT_EQ(input, expected);
}

int main(int argc, char **argv) {
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS(); 
}