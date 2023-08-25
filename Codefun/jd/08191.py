# 判断九宫格 直接遍历即可

""" 输入
3
...
o*o
...
...
*o*
...
o..
*..
o..
"""

""" 输出
yukari
kou
yukari
"""
n = int(input())


def solve(g):
    yukari, kou = False, False
    for line in g:
        if line == "o*o":
            yukari = True
        if line == "*o*":
            kou = True

    for column in zip(*g):
        column = "".join(c for c in column)
        if column == "o*o":
            yukari = True
        if column == "*o*":
            kou = True

    # 题目倒是讲清楚啊...
    if not (yukari or kou):
        return "draw"
    return "draw" if yukari and kou else "yukari" if yukari else "kou"


for i in range(n):
    g = []
    for j in range(3):
        g.append(input())
    ans = solve(g)
    print(ans)
