"""LeetCode 2591：将钱分给最多的儿童。"""


class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1

        money -= children
        exact = min(money // 7, children)
        remainder = money - 7 * exact
        remaining_children = children - exact

        # 剩余的钱必须分完，也不能让唯一剩下的孩子得到 4 元。
        if (remaining_children == 0 and remainder > 0) or (remaining_children == 1 and remainder == 3):
            exact -= 1
        return exact


if __name__ == "__main__":
    solution = Solution()
    assert solution.distMoney(16, 2) == 2
    assert solution.distMoney(20, 3) == 1
    assert solution.distMoney(2, 3) == -1
