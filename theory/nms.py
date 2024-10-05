import numpy as np


# det[x1, y2, x2, y2, scores]
def nms(dets, iou_thred, cfd_thred):
    if len(dets) == 0:
        return []
    bboxes = np.array(dets)
    ## 维护orders
    orders = np.argsort(bboxes[:, 4])
    pick_bboxes = []
    x1 = bboxes[:, 0]
    y1 = bboxes[:, 1]
    x2 = bboxes[:, 2]
    y2 = bboxes[:, 3]
    areas = (x2 - x1 + 1) * (y2 - y1 + 1)  ## 提前计算好bboxes面积，防止在循环中重复计算

    while orders.shape[0] and bboxes[orders[-1], -1] >= cfd_thred:
        bbox = bboxes[orders[-1]]
        xx1 = np.maximum(bbox[0], x1[orders[:-1]])
        yy1 = np.maximum(bbox[1], y1[orders[:-1]])
        xx2 = np.minimum(bbox[2], x2[orders[:-1]])
        yy2 = np.minimum(bbox[3], y2[orders[:-1]])
        inters = np.maximum(xx2 - xx1 + 1, 0) * np.maximum(yy2 - yy1 + 1, 0)
        unions = areas[orders[-1]] + areas[orders[:-1]] - inters
        ious = inters / unions
        keep_indices = np.where(ious < iou_thred)
        pick_bboxes.append(bbox)
        orders = orders[keep_indices]
    return np.asarray(pick_bboxes)


dets = [[187, 82, 337, 317, 0.9], [150, 67, 305, 282, 0.75], [246, 121, 368, 304, 0.8]]
dets_nms = nms(dets, 0.5, 0.3)
print(dets_nms)


pow()
