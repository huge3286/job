# 优化 实际上就是找一个最接近 sum/2 的矩阵和
# 短边求和长边二分？
# 在确认左上角之后可以二分求出最佳的矩阵
n, m = map(int, input().split())
matrix = []
pre = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n):
    matrix.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        pre[i + 1][j + 1] = pre[i + 1][j] + pre[i][j + 1] - pre[i][j] + matrix[i][j]

sum_ = pre[-1][-1]

ans = float("inf")
for x in range(n):
    for y in range(m):
        l = min(n - x, m - y)
        for d in range(l + 1):
            i = x + d
            j = y + d
            square = pre[i][j] + pre[x][y] - pre[i][y] - pre[x][j]
            ans = min(ans, abs(sum_ - 2 * square))

print(ans)


"""
3 3
9 9 8 
2 4 4
3 5 3
"""
