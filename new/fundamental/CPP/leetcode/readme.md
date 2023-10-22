# 环境配置
进入 [力扣官网](https://leetcode.cn/) 注册账号即可

# Hello World
下面演示如何使用cpp实现$Hello World$，介绍cpp编程的基本框架

```cpp
#include <iostream>  // 导入名为iostream的包 提供输入输出功能

int main() {  // 定义主函数 输出类型为int(integer)
    std::cout << "Hello World" << std::endl;  // 调用cout函数输出
    return 0;  // 必须返回结果 填几都无所谓没意义
}
```

# Two Sum
下面演示leetcode做题方法 以第一题两数之和为例子
```cpp
class Solution {  // 定义一个Solution类 leetcode所有题目都是这样
public:
    // 根据给的输入和输出 编写函数体
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        for (int i=0; i<n-1; i++) {
            for (int j=i+1; j<n; j++) {
                if (nums[i]+nums[j] == target)
                return {i, j};  // return返回结果即可
            }
        }
        return {-1, -1};
    }
};
```
