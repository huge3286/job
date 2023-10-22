# 华为秋招第二场 第三题

n = int(input())
cache = list(map(int, input().split()))
indegrees = [0] * n
g = [[] for _ in range(n)]

for cur in range(n):
    for pre, symbol in enumerate(input().split()):
        if symbol == "1":
            indegrees[cur] += 1
            g[pre].append(cur)

from collections import deque

q = deque([i for i, indegree in enumerate(indegrees) if indegree == 0])

ans = 0
while q:
    res = 0
    for _ in range(len(q)):
        u = q.popleft()
        res += cache[u]

        for v in g[u]:
            indegrees[v] -= 1
            if indegrees[v] == 0:
                q.append(v)

    ans = max(ans, res)

print(ans)
