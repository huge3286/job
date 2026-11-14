n, m = map(int, input().split())  # 数的个数和目标数字和
a = list(map(int, input().split()))


# 从i开始选 返回数字的个数
def f(i, c):
    if c == 0:
        return 0
    if i >= n:
        return float("inf")
    return min(f(i + 1, c - a[i]) + 1, f(i + 1, c))


print(f(0, m))


# 递推数组

n, m = map(int, input().split())
a = list(map(int, input().split()))
f = [1e9 for i in range(0, m + 1)]
f[0] = 0
for i in range(0, n):
    for j in range(m, a[i] - 1, -1):
        f[j] = min(f[j], f[j - a[i]] + 1)
if f[m] == 1e9:
    print("No solution")
else:
    print(f[m])
