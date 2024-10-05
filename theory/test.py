class Solution:
    def distMoney(self, money: int, children: int) -> int:
        def check(c):
            m = money - c * 8  # 剩下的钱
            if m < children - c:
                return False
            if children - c == 1 and m == 4:
                return False
            return True

        l, r = 0, children
        ans = 0
        while l <= r:
            m = (l + r) // 2
            if check(m):
                ans = m
                l = m + 1
            else:
                r = m - 1

        return ans


s = Solution()
s.distMoney(16, 2)
