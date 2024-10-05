n, m = map(int, input().split())
prices = list(map(int, input().split()))
coupon = []
for i in range(m):
    coupon.append(list(map(int, input().split())))
coupon.sort()

for i in range(1, m):  # DP求出最优的优惠券
    coupon[i][1] = max(coupon[i - 1][1], coupon[i][1])

a = [i for i, j in coupon]
from bisect import bisect_right

ans = 0
for price in prices:
    coupon_idx = bisect_right(a, price) - 1
    if coupon_idx == -1:
        ans += price
    else:
        ans += price - coupon[coupon_idx][1]

print(ans)

"""
3 3
4 6 8
3 2
4 3
9 5

9
"""
