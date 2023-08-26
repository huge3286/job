n = int(input())
g = [[] for i in range(n)]
for i in range(n - 1):
    u, v = map(int, input.split())
    g[u - 1].append(v - 1)
    g[v - 1].append(u - 1)


class Tree:
    def __init__(son, far, portal):
        self.son = son
        self.far = far
        self.portal = portal


# form tree
def dfs(cur, far):
    res, idx = float("inf"), -1
    for son in g[cur]:
        if son == far:
            continue
