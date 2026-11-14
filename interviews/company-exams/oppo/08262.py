n = int(input())
g = []

for i in range(n):
    g.append(input())


def solve(line):
    n = len(line)
    ans = 0
    res = 1
    for i in range(1, n):
        if line[i] != line[i - 1]:
            ans += res * (res - 1)
            res = 1
        else:
            res += 1

    return ans + res * (res - 1)


ans = 0
for line in g:
    ans += solve(line)

for column in zip(*g):
    ans += solve(column)



print(ans)
