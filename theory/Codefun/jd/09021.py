n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(min(m, sum(min(i, j) for i, j in zip(a, b))))
