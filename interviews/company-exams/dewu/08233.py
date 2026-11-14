""" 读取数据 建图 """
n, m = map(int, input().split())

edges = []
for i in range(m):
    x, y, c = map(int, input().split())
    edges.append([x - 1, y - 1, c])


""" 并查集模板 """
fa = list(range(n))


def find(x):
    return x if fa[x] == x else find(fa[x])


""" 按照积分从大到小枚举 """
ans = 0
cnt = 1
for x, y, c in sorted(edges, key=lambda x: x[2], reverse=True):
    fx, fy = map(find, (x, y))
    if fx != fy:
        ans += c
        cnt += 1
        fa[fx] = fy

    if cnt == n:
        print(ans)
        exit()

print("No solution.")
