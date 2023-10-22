n = int(input())
m = int(input())
x, y = map(int, input().split())

g = []
for i in range(m):
    g.append(list(map(int, input().split())))

dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

time = [[float("inf")] * n for _ in range(m)]
time[x][y] = 0

# bfs
from collections import deque

q = deque([[x, y]])
while q:
    x, y = q.popleft()
    for dx, dy in dir:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx > m - 1 or ny < 0 or ny > n - 1 or g[nx][ny] == 0:
            continue
        nt = time[x][y] + g[x][y]  # 到达下一个节点的时间
        if time[nx][ny] > nt:
            time[nx][ny] = nt
            q.append([nx, ny])


ans = 0
out_flag = 0
for i in range(m):
    for j in range(n):
        if time[i][j] < float("inf"):
            ans = max(ans, time[i][j])
        elif g[i][j] > 0:
            ans = -1
            out_flag = 1
            break
    if out_flag:
        break

print(ans)
