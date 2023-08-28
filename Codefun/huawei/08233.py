n = int(input())
m = int(input())
x, y = map(int, input().split())

g = []
for i in range(m):
    g.append(list(map(int, input().split())))

dir = [[0, -1], [-1, 0], [0, 1], [1, 0]]

from collections import deque

ans = [[0] * n for _ in range(m)]

for i in range(m):
    for j in range(n):
        if g[i][j] != 0:
            ans[i][j] = float("inf")

# bfs
res = 0
q = deque([[x, y, 0]])
while q:
    x, y, t = q.popleft()
    if -1 < x < m and -1 < y < n and g[x][y] != 0:
        if t > ans[x][y]:
            continue
        ans[x][y] = t

        for dx, dy in dir:
            q.append([x + dx, y + dy, t + g[x][y]])

res = 0
for line in ans:
    for item in line:
        if item < float("inf"):
            res = max(res, item)
        else:
            res = -1
            break

print(res)
