n, T = map(int, input().split())

timu = []
for i in range(n):
    timu.append(list(map(int, input().split())))

# 做到i题能够得到的最高分数

dp = [[[-float('inf')] * 3 for _ in range(T+1)] for _ in range(n)]
t1, s1, t2, s2 = timu[i]
dp[0][T][0] = 0
dp[0][T-t1][1] = s1
dp[0][T-t2][2] = s2

for i in range(1, n):
    t1, s1, t2, s2 = timu[i]
    for j in range(T+1):
        dp[i][j][0] = max(dp[i-1][j])
        dp[i][j][1] = (max(dp[i-1][j-t1]) + s1) if j > t1 else -float('inf')
        dp[i][j][2] = (max(dp[i-1][j-t2]) + s2) if j > t2 else -float('inf')

print(dp)
