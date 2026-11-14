"""以 1 为根，按顺序覆盖子树节点权值，最后求和。"""


def final_sum(values, edges, assignments):
    n = len(values)
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # 每个节点只受自己或祖先的操作影响。先记下各节点最后一次操作。
    updates = {}
    for time, (node, value) in enumerate(assignments):
        updates[node] = time, value

    total = 0
    stack = [(1, 0, (-1, 0))]
    while stack:
        node, parent, inherited = stack.pop()
        latest = updates.get(node, (-1, 0))
        if inherited[0] > latest[0]:
            latest = inherited
        total += latest[1] if latest[0] >= 0 else values[node - 1]
        stack.extend((child, node, latest) for child in graph[node] if child != parent)
    return total


if __name__ == "__main__":
    n = int(input())
    values = list(map(int, input().split()))
    edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
    assignments = (tuple(map(int, input().split())) for _ in range(int(input())))
    print(final_sum(values, edges, assignments))
