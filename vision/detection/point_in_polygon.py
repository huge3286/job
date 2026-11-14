"""用射线奇偶规则测试多边形，可包含内环。边界视为内部。"""

from math import isclose


def isRayIntersectsSegment(poi, s_poi, e_poi):
    x, y = poi
    x1, y1 = s_poi
    x2, y2 = e_poi
    if (y1 > y) == (y2 > y):
        return False
    crossing = x1 + (x2 - x1) * (y - y1) / (y2 - y1)
    return crossing > x


def isPoiWithinPoly(poi, poly):
    x, y = poi
    inside = False
    for ring in poly:
        if len(ring) < 3:
            continue
        for index, end in enumerate(ring):
            start = ring[index - 1]
            x1, y1 = start
            x2, y2 = end
            cross = (x2 - x1) * (y - y1) - (y2 - y1) * (x - x1)
            if (isclose(cross, 0, abs_tol=1e-9)
                    and min(x1, x2) <= x <= max(x1, x2)
                    and min(y1, y2) <= y <= max(y1, y2)):
                return True
            if isRayIntersectsSegment(poi, start, end):
                inside = not inside
    return inside


if __name__ == "__main__":
    outer = [(0, 0), (4, 0), (4, 4), (0, 4)]
    hole = [(1, 1), (3, 1), (3, 3), (1, 3)]
    assert isPoiWithinPoly((0, 2), [outer, hole])
    assert isPoiWithinPoly((0.5, 2), [outer, hole])
    assert not isPoiWithinPoly((2, 2), [outer, hole])
    assert not isPoiWithinPoly((5, 2), [outer])
