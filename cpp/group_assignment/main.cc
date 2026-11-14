#include <algorithm>
#include <iostream>
#include <unordered_map>
#include <vector>

int minGroupsForValidAssignment(const std::vector<int>& nums) {
    if (nums.empty()) {
        return 0;
    }

    std::unordered_map<int, int> counts;
    int min_count = static_cast<int>(nums.size());
    for (int num : nums) {
        ++counts[num];
    }
    for (const auto& entry : counts) {
        min_count = std::min(min_count, entry.second);
    }

    // 组大小只能是 size 或 size + 1，优先试最大的可行 size。
    for (int size = min_count; size >= 1; --size) {
        int total = 0;
        bool feasible = true;
        for (const auto& entry : counts) {
            int count = entry.second;
            int groups = (count - 1) / (size + 1) + 1;
            if (groups > count / size) {
                feasible = false;
                break;
            }
            total += groups;
        }
        if (feasible) {
            return total;
        }
    }
    return static_cast<int>(nums.size());
}

int main() {
    const std::vector<int> original = {3, 2, 3, 2, 3};
    const std::vector<int> regression = {1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2};
    if (minGroupsForValidAssignment(original) != 2 ||
        minGroupsForValidAssignment(regression) != 4 ||
        minGroupsForValidAssignment({}) != 0) {
        std::cerr << "Group assignment check failed\n";
        return 1;
    }
    std::cout << minGroupsForValidAssignment(regression) << '\n';
}
