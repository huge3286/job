"""串行执行所有任务所需的最低初始电量。每个任务输入为 耗电量:启动阈值。"""


def minimum_charge(missions):
    normalized = [(cost, max(cost, threshold)) for cost, threshold in missions]
    spent = required = 0
    for cost, threshold in sorted(normalized, key=lambda task: task[1] - task[0], reverse=True):
        required = max(required, spent + threshold)
        spent += cost
    return required


if __name__ == "__main__":
    missions = [tuple(map(int, mission.split(":"))) for mission in input().split(",")]
    charge = minimum_charge(missions)
    print(charge if charge <= 4800 else -1)
