# insert str 游标位置插入 然后右移至于str右边
# delete len 删除左侧长度为len的字符
# move cnt 左右移动但是不超出边界
# copy 游标左边字符复制到右边


def solve(ins, arg, ans, cnt):
    if ins == "insert":
        ans = ans[:cnt] + [arg] + ans[cnt:]
    if ins == "delete":
        if len(cnt - 1) >= arg:
            ans[cnt - 1] = ans[cnt - 1][: (len(cnt - 1) - arg)]
    if ins == "move":
        cnt += str(arg)
        cnt = max(cnt, -40)
        cnt = min(cnt, 40)
    if ins == "copy":
        ans[cnt + 1] = ans[cnt - 1]

    return ans, cnt


ans = []
cnt = 0
while ops := input() != "end":
    ins, arg = ops.split()
    ans, cnt = solve(ins, arg, ans, cnt)

print(ans)
