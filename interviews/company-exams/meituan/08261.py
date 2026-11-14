# 浇水成长值 施肥成长值 成熟的成长值
x, y, z = map(int, input().split())

symbol = 0
t = 0
while z > 0:
    z -= x
    if not symbol:
        z -= y
        symbol = 2
    else:
        symbol -= 1
    t += 1

print(t)