n, k = map(int, input().split())
nums = list(input())

res = 0
for i in range(n):
    if k == 0:
        break

    if nums[i] == "1":
        res += 1
    else:
        if res <= k:
            nums[i - res], nums[i] = "0", "1"
            k -= res
        else:
            nums[i - k], nums[i] = "0", "1"
            k = 0
        res = 0


print("".join(num for num in nums))
