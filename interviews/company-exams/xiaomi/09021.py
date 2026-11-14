n = int(input())
shelves = []
for i in range(n):
    shelves.append(list(map(int, input().split())))
balloons = list(zip(*shelves))

from functools import cache


# 剩m元 买第i个气球
@cache
def dfs(i, m):
    if i < 4 and m <= 0:  # 剪枝
        return 0
    if i == 4:
        return 1 if m == 0 else 0
    res = 0
    for balloon in balloons[i]:
        res += dfs(i + 1, m - balloon)
    return res


print(dfs(0, 1000))

"""
2
250 250 250 250
150 250 450 150

"""
