import sys


class Node:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

    def __lt__(self, other):
        return self.w > other.w


def find(x):
    return x if fa[x] == x else find(fa[x])


def merge(x, y):
    fx = find(x)
    fy = find(y)
    if fx != fy:
        fa[fx] = fy


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    e = [Node(0, 0, 0) for i in range(0, m)]
    for i in range(0, m):
        u, v, w = map(int, sys.stdin.readline().split())
        e[i] = Node(u, v, w)
    fa = [i for i in range(0, m + 1)]
    e.sort()
    cnt = 1
    ans = 0
    for i in range(0, m):
        u = e[i].u
        v = e[i].v
        w = e[i].w
        if find(u) != find(v):
            merge(u, v)
            cnt += 1
            ans += w
            if cnt == n:
                print(ans)
                exit()
    print("No solution.")
