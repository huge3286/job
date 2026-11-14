# 前缀和
# 积之和 很好的思路
def solve():
    s = input()  # 输入字符串 s
    mod = 998244353  # 定义常数 mod
    ans = 0  # 初始化答案 ans

    # 遍历字母表的每个字母
    for i in range(26):
        pre = 0  # 初始化前缀和 pre
        for j in range(1, len(s)):
            pre = (pre * 2) % mod  # 左移一位，相当于乘以 2，然后对前缀和取模
            if ord(s[j - 1]) - ord("a") == i:
                pre += 1  # 如果前一个字符是当前字母，增加前缀和
            if ord(s[j]) - ord("a") == i:
                ans += pre  # 如果当前字符是当前字母，增加答案 ans
            ans %= mod  # 对答案取模

    ans += len(s)  # 最后加上字符串长度
    ans %= mod  # 对答案再次取模
    print(ans)  # 输出答案


if __name__ == "__main__":
    solve()  # 调用解决函数
