nums = []
for i in range(3):
    nums.append(list(map(int, input().split())))
nums.sort(key=lambda x: x[1])

if nums[1][1] >= nums[2][0]:
    print(nums[1][1])
elif nums[0][1] >= nums[1][0]:
    print(nums[0][1])
else:
    print(-1)
