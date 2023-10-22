"""
动态规划 从(i, j)出发的最少步数
"""
n, m = list(map(int, input().split()))
g = []
for _ in range(n):
    g.append(input())

# 注意应该初始化为最大值'inf'
f = [[[float("inf")] * 3 for _ in range(m)] for _ in range(n)]

f[0][0] = [1] * 3
for i in range(n):
    for j in range(m):
        if g[i][j] == "*" or (i == 0 and j == 0):
            continue
        f[i][j][0] = min(f[i - 1][j][0], f[i - 1][j][1] + 1, f[i - 1][j][2] + 1)
        f[i][j][1] = min(f[i][j - 1][0] + 1, f[i][j - 1][1], f[i][j - 1][2] + 1)
        f[i][j][2] = min(f[i - 1][j - 1][0] + 1, f[i - 1][j - 1][1] + 1, f[i - 1][j - 1][2])

print(min(f[n - 1][m - 1]))

"""
递归版本
"""
n, m = list(map(int, input().split()))
g = []
for _ in range(n):
    g.append(input())

from functools import cache


# 设置第3位 表示上一步的方向 如果方向不变则不需增加步数
# 0代表向下 1代表向右 2代表右下
@cache
def f(i, j, d):
    if i == n - 1 and j == m - 1:
        return 0

    if -1 < i < n and -1 < j < m and g[i][j] == ".":
        if d == 0:
            return min(f(i + 1, j, 0), f(i, j + 1, 1) + 1, f(i + 1, j + 1, 2) + 1)
        elif d == 1:
            return min(f(i + 1, j, 0) + 1, f(i, j + 1, 1), f(i + 1, j + 1, 2) + 1)
        else:
            return min(f(i + 1, j, 0) + 1, f(i, j + 1, 1) + 1, f(i + 1, j + 1, 2))
    else:
        return float("inf")


print(min(f(0, 0, 0), f(0, 0, 1), f(0, 0, 2)) + 1)
