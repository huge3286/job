n = int(input())
a = input()

g = [[] for i in range(n)]
o = [0] * n  # 保存每个节点附近o的数量

for i in range(n - 1):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    g[u].append(v)
    g[v].append(u)
    o[u] += 1 if a[v] == 'o' else 0
    o[v] += 1 if a[u] == 'o' else 0

# x和z分别代表当前节点和上一个节点
def dfs(x, z):
    res = 0
    # 如果出现了连续的p 就求oppo的数量
    if z != -1 and a[x] == "p" and a[z] == "p":
        res += o[x] * o[z]

    # 继续递归
    for y in g[x]:
        if y == z:
            continue
        res += dfs(y, x)

    return res


ans = dfs(0, -1)

print(ans * 2)
