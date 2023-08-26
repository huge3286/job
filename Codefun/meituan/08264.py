# 求平均数正好等于k的最长连续数组

n, k = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
    a[i] -= k

from itertools import accumulate

p = list(accumulate(a, initial=0))


from collections import defaultdict

# 值和下标
d = defaultdict(int)
ans = -1
for index, item in enumerate(p):
    if item in d:
        ans = max(ans, index - d[item])
    else:
        d[item] = index

print(ans)
