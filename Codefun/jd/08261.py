n = int(input())
a = list(map(int, input().split()))
b = []

s = set()
for index, item in enumerate(a):
    # 1. a+b 是index+1的倍数
    # 2. b > 0
    # 3. b 不能重复
    k = item // (index + 1) + 1
    new_b = k * (index+1) - item
    while new_b in s:
        k += 1
        new_b = k * (index+1) - item
    s.add(new_b)
    b.append(new_b)

print(''.join(str(i)+' ' for i in b))
