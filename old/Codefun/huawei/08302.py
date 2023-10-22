# 算出到底是多少次方
n = int(input())
x = 1
while 2**x < n:
    x += 1

leaf = list(map(int, input().split()))

# 每个节点的数值为 叶节点的最大最小值的平均值 - 父节点
# 输出二叉树数组

# 第i层的第j的元素
# 数量满足 2^i = j

ans = [0] * (2 ** (x + 1) - 1)
from functools import cache


# 建树求出每个节点的最大最小值
@cache
def dfs(i, j):
    if i == x:
        ans[2**i + j - 1] = leaf[j]
        return leaf[j], leaf[j]
    mi1, ma1 = dfs(i + 1, 2 * j)
    mi2, ma2 = dfs(i + 1, 2 * j + 1)

    mi = min(mi1, mi2)
    ma = max(ma1, ma2)

    ans[2**i + j - 1] = (mi + ma) // 2

    return mi, ma


dfs(0, 0)


# dfs带着所有父节点的和递推
def dfs(i, j, f):
    if i > x:
        return

    ans[2**i + j - 1] -= f
    dfs(i + 1, 2 * j, f + ans[2**i + j - 1])
    dfs(i + 1, 2 * j + 1, f + ans[2**i + j - 1])


dfs(0, 0, 0)

print(*ans)
