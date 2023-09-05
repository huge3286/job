missions = [list(map(int, mission.split(":"))) for mission in input().split(",")]
missions.sort(key=lambda x: x[1] - x[0])

d = 0  # 多留出的余量
for i in range(len(missions) - 1):
    consume, threshold = missions[i]
    pre_bound = missions[i + 1][1] - missions[i + 1][0]  # 上一个任务执行完的最低电量
    d += max(0, threshold - pre_bound - d)  # 如果电量不足 就再充一些

ans = max(sum(m[0] for m in missions), missions[-1][1] + d)
print(ans if ans <= 4800 else -1)
"""
1:9,2:7,3:5


任务需要消耗的电量：要求的最低电量
求串行执行所有任务需要的电量
"""
