n, m = map(int, input().split())

g = []
for i in range(n):
    s, a = input().split()
    s = 1 if s == 'human' else 0
    a = int(a)
    g.append([s, a])

for i in range(m):
    # Y代表身份是公开的 N是隐藏的
    try:
        u, v, c1, c2 = input().split()
    except:
        continue
    u, v = map(int, (u, v))
    u, v = u-1, v-1
    s1, s2 = g[u][0], g[v][0]
    k1, k2 = g[u][1], g[v][1]
    # 身份相同 或 一方死亡 或 都不知道身份 则没有打架
    if s1 == s2 or s1 == -1 or s2 == -1 or (c1 == 'N' and c2 == 'N'):
        continue
    # 如果s1是人
    if s1 == 1:
        # s1身份暴露
        if c1 == 'Y':
            if k1 <= k2:
                g[u][0] = -1
            if k1 >= k2:
                g[v][0] = -1
        
        # s2暴露且攻击力更高
        elif c2 == 'Y' and k1 > k2:
            g[v][0] = -1
        else:
            continue

    # 如果s2是人
    else:
        if c2 == 'Y':
            if k1 <= k2:
                g[u][0] = -1
            if k1 >= k2:
                g[v][0] = -1
        elif c1 == 'Y' and k2 > k1:
            g[u][0] = -1
        else:
            continue



print(''.join('Y' if i[0] != -1 else 'N' for i in g))