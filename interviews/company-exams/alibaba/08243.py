n = int(input())
g = [[] for i in range(n)]
for i in range(n - 1):
    u, v = map(int, input().split())
    g[u - 1].append(v - 1)
    g[v - 1].append(u - 1)

dp, portal = [0] * n, [0] * n


# 以x为节点的子树的最小节点
def dfs(x, fa):
    min_ = 1e6

    for y in g[x]:
        if y == fa:
            continue
        min_ = min(min_, dfs(y, x))

    # 更新传送门
    portal[x] = min_

    # 说明是叶子节点 只能获取当前位置的积分
    if portal[x] == 1e6:
        dp[x] = 1
    else:
        dp[x] = dp[portal[x]] + 1

    return min(min_, x)  # 为什么要在最后更新一次


dfs(0, -1)

print("".join(str(i) + " " for i in dp))
