n, T = map(int, input().split())

timu = []
for i in range(n):
    timu.append(list(map(int, input().split())))


from collections import deque
def bfs():
    # 题号 时间 分数
    q = deque([[0, T, 0, ""]])
    res = 0

    while q:
        i, t, s, path = q.popleft()
        if i == n or t == 0:
            if s > res:
                res = s
                ans = path
        else:
            t1, s1, t2, s2 = timu[i]
            q.append((i + 1, t, s, path + "F"))
            if t >= t1:
                q.append((i + 1, t - t1, s + s1, path + "A"))
            if t >= t2:
                q.append((i + 1, t - t2, s + s2, path + "B"))

    return ans


ans = bfs()

print(ans)
