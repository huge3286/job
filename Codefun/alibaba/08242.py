# 看清题目
# 想清楚要求解的问题
# 不然也是白搭

n = int(input())
a = list(map(int, input().split()))
mod = 10**9 + 7
from collections import Counter

a = list(Counter(a).items())
a.sort()

mul = 1
ans = 0
for i, (num, freq) in enumerate(a):
    if num != i + 1:
        break
    mul *= freq
    ans += mul

print(ans % mod)
