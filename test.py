n, m = map(int, input().split())  # n个电子元件 m对电子元件分数

g = [[] for i in range(n)]
for i in range(m):
    u, v, num = map(int, input().split())
    g[u - 1].append((v - 1, num))
    g[v - 1].append((u - 1, num))


def bfs(cur, visited):
    queue = [(cur, 0, visited)]  # 初始节点、分数和visited
    max_score = 0

    while queue:
        cur, score, cur_visited = queue.pop(0)
        max_score = max(max_score, score)
        cur_visited |= 1 << cur  # 更新当前节点的访问状态

        for nxt, cre in g[cur]:
            if not (cur_visited & (1 << nxt)):
                queue.append((nxt, score + cre, cur_visited))

    return max_score


ans = 0
for i in range(n):
    visited = 0  # 使用整数来表示访问状态
    ans = max(ans, bfs(i, visited))

print(ans)
