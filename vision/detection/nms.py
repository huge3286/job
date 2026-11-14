"""贪心非极大值抑制。每一行是 [x1, y1, x2, y2, score]。"""

import numpy as np


def nms(dets, iou_thred, cfd_thred, *, offset=1):
    """返回按置信度递减保留的框。整数像素闭区间用 offset=1，连续坐标用 0。"""
    boxes = np.asarray(dets, dtype=float).reshape(-1, 5)
    candidates = np.flatnonzero(boxes[:, 4] >= cfd_thred)
    order = candidates[np.argsort(-boxes[candidates, 4], kind="stable")]
    areas = np.maximum(boxes[:, 2:4] - boxes[:, :2] + offset, 0).prod(axis=1)
    keep = []
    while order.size:
        first, rest = order[0], order[1:]
        keep.append(first)
        starts = np.maximum(boxes[first, :2], boxes[rest, :2])
        ends = np.minimum(boxes[first, 2:4], boxes[rest, 2:4])
        intersection = np.maximum(ends - starts + offset, 0).prod(axis=1)
        union = areas[first] + areas[rest] - intersection
        iou = np.divide(intersection, union, out=np.zeros_like(intersection), where=union > 0)
        order = rest[iou <= iou_thred]
    return boxes[keep]


if __name__ == "__main__":
    dets = [[187, 82, 337, 317, 0.9], [150, 67, 305, 282, 0.75], [246, 121, 368, 304, 0.8]]
    result = nms(dets, 0.5, 0.3)
    assert np.allclose(result[:, 4], [0.9, 0.8])
    print(result)
