n = int(input())
m = int(input())
x, y = map(int, input().split())

g = []
for i in range(m):
    g.append(list(map(int, input().split())))

dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

res = [[float("inf")] * n for _ in range(m)]

# bfs
from collections import deque

q = deque([[x, y, 0]])
while q:
    x, y, t = q.popleft()

    if -1 < x < m and -1 < y < n and g[x][y] != 0:
        if t >= res[x][y]:
            continue

        res[x][y] = t

        for dx, dy in dir:
            q.append([x + dx, y + dy, t + g[x][y]])

ans = 0
out_flag = 0
for i in range(m):
    for j in range(n):
        if res[i][j] < float("inf"):
            ans = max(ans, res[i][j])
        elif g[i][j] > 0:
            ans = -1
            out_flag = 1
            break
    if out_flag:
        break

print(ans)
