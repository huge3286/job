# 两个长为n的数组a和b
# 重排a数组使得 1 <= a_i + b_i <= m

q = int(input())


def check(a, b, m):
    for x, y in zip(a, b):
        if not 1 <= x + y <= m:
            return False
    return True


for _ in range(q):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort(reverse=True)
    print("Yes" if check(a, b, m) else "No")
