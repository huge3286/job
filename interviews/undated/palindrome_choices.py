"""逐位置从两个字符串中选字符，统计能组成的不同回文串。"""

MOD = 10**9 + 7


def count_palindromes(a, b):
    result = 1
    for left in range(len(a) // 2):
        right = len(a) - 1 - left
        common = {a[left], b[left]} & {a[right], b[right]}
        result = result * len(common) % MOD
    if len(a) % 2:
        middle = len(a) // 2
        result = result * len({a[middle], b[middle]}) % MOD
    return result


if __name__ == "__main__":
    n = int(input())
    a, b = input(), input()
    if len(a) != n or len(b) != n:
        raise ValueError("输入字符串长度与 n 不一致")
    print(count_palindromes(a, b))
