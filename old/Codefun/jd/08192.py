"""
位运算维护当前的bug数量

注意bit_count()是 python 3.10才有的功能
之前的版本建议移位统计
"""

n = int(input())  # len(bugs)
bug = int(input(), 2)  # bugs
m = int(input())  # len(tools)

tools = []
for _ in range(m):
    # 按照二进制数读取 int(*, 2)
    toolFix = int(input(), 2)
    toolBug = int(input(), 2)
    tools.append((toolFix, toolBug))

# 输出t个整数表示当前的bug数量
t = int(input())  # num tools
for i in range(t):
    toolIdx = int(input()) - 1
    bug -= bug & tools[toolIdx][0]
    bug = bug | tools[toolIdx][1]  # 当前的bug和产生的bug取并集合

    print(bug.bit_count())
