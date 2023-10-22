"""
第三题

5
aabcb
acbaa
"""

n = int(input())
a = input()
b = input()
mod = 10**9 + 7

ans = 1
for i in range(n // 2):
    res = 0
    if a[n - i - 1] in (a[i], b[i]):
        res += 1
    if b[n - i - 1] in (a[i], b[i]):
        res += 1
    if b[n - i - 1] == a[n - i - 1]:
        res -= 1

    # 你加这个看看 好像是没考虑到为0的情况
    res = max(res, 0)

    ans *= res

print(ans)
