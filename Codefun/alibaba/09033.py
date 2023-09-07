import sys

sys.setrecursionlimit(100000)
n = int(input())
a = list(map(int, input().split()))

pa = list(range(n))


def find(x):
    return x if pa[x] == x else find(pa[x])


def merge(x: int, y: int):
    pa[find(y)] = find(x)


for _ in range(n - 1):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    if a[u] == a[v]:
        merge(u, v)

d = dict()
for i in range(n):
    d[find(i)] = d.get(find(i), 0) + 1

p = 0
ans = 0
for k, v in d.items():
    if a[k] == 3:
        ans += v * (v - 1) // 2 * 3
    else:
        ans += v * (v - 1) // 2 * 5
    p += 15 * (n - v) * v

print(ans + p // 2)
