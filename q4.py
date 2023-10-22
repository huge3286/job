"""
3
1 2 3
1 2
2 3
1
2 4
"""

n = int(input())
a = list(map(int, input().split()))

g = [[] for i in range(n + 1)]
for i in range(n - 1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)


from collections import deque

tree = [[] for i in range(n + 1)]

# 建树
dq = deque([[1, -1]])

while dq:
    u, w = dq.popleft()
    for v in g[u]:
        if w == v:
            continue
        dq.append([v, u])
        tree[u].append(v)


q = int(input())
for i in range(q):
    u, x = map(int, input().split())

    dq = deque([u])
    while dq:
        u = dq.popleft()
        a[u - 1] = x
        for v in tree[u]:
            dq.append(v)

print(sum(a))
