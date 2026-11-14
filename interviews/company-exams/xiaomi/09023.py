"""小米手机通信校准。输入目标频道，再输入升序的 频道:损失 对。"""

from bisect import bisect_left


def nearest_loss(target, measurements):
    index = bisect_left(measurements, target, key=lambda pair: pair[0])
    if index == 0:
        return measurements[0][1]
    if index == len(measurements):
        return measurements[-1][1]

    left_frequency, left_loss = measurements[index - 1]
    right_frequency, right_loss = measurements[index]
    left_distance = target - left_frequency
    right_distance = right_frequency - target
    if left_distance == right_distance:
        return (left_loss + right_loss) / 2
    return left_loss if left_distance < right_distance else right_loss


if __name__ == "__main__":
    target = int(input())
    measurements = [tuple(map(int, pair.split(":"))) for pair in input().split()]
    print(f"{nearest_loss(target, measurements):.1f}")
