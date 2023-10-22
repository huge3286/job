n = int(input())


def solve(n):
    ans = "oppo"
    if n <= 4:
        return ans[:n]

    for i in range((n - 4) // 3):
        ans += 'ppo'

    return ans

ans = solve(n)
print(ans + ''.join('p' for i in range(n-len(ans))))
