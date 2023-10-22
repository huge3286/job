# 账单数n和除小红以外的总人数m
n, m = map(int, input().split())

# 返回m个人要转的钱
ans = [0] * m
for i in range(n):
    # 一起吃饭的人数 花费
    k, c = map(int, input().split())
    nums = list(map(int, input().split()))
    p = c // k + (1 if c % k != 0 else 0)
    for num in nums:
        ans[num-1] += p 

print(''.join(str(i)+' ' for i in ans))
