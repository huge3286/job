# N个节点 t个端口 节点的每个端口进行了连通块的划分

# A有m个端口
m, *port = list(map(int, input().split()))

s = set()
for p in port:
    s.add(p)

# 除A之外还有其他n个节点
n = int(input())

ans = []
for i in range(n):
    name, num, *node = list(map(int, input().split()))
    for j in node:
        if j in s:
            ans.append(name)
            break

print(len(ans))
print(*sorted(ans))
