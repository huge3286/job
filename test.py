n, v = 6, 10
a = [4 ,-2 ,-11 ,-1 ,4 ,-1]
def solve(n, v, a):
    ans = -1e9
    # 初始条件
    res = a[0]
    min_idx = 0
    for i in range(1, len(a)):

        # 另起炉灶
        if res < 0:
            res = a[i]
            min_idx = i
        else:
            res += a[i]
            if a[min_idx] > a[i]:
                min_idx = i
        ans = max(res - a[min_idx] + v, res, ans)
    return ans

solve(n, v, a)