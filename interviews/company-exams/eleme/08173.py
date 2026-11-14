import heapq
from collections import defaultdict

INF = float("inf")


def main():
    n, m, T = map(int, input().split())

    g = defaultdict(list)
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append((v, w))
        g[v].append((u, w))

    q = [(0, 0)]

    vis = [0] * n
    dist = [INF] * n
    dist[0] = 0

    while q:
        dist_u, u = heapq.heappop(q)
        if vis[u]:
            continue
        vis[u] = 1

        # 迪迦算法 每个节点只需要枚举一次
        # 与bfs的区别在于 只有在确认了路径是更优的情况 才会加入堆
        # 每进去一个新节点 会更新其它所有相邻节点的最优解
        for v, w in g[u]:
            if dist[v] > dist_u + w:
                dist[v] = dist_u + w
                heapq.heappush(q, (dist[v], v))

    places = list(map(int, input().split()))
    ans = sum(dist[i - 1] for i in places)

    print(ans * 2)


if __name__ == "__main__":
    main()
