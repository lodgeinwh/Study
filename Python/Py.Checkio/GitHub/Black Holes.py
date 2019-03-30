# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: Black Holes.py
# @time: 2019/02/27 20:04:51
# @contact: lodgeinwh@gmail.com
# @version: 1.0


def checkio(data):
    from math import pi, sqrt, acos, degrees
    from itertools import combinations

    def distance(data):
        x1, y1, r1 = data[0]
        x2, y2, r2 = data[1]
        return sqrt((x1 - x2)**2 + (y1 - y2)**2)

    def intersection_area(data):
        ro1, ro2 = data
        if ro1[2] < ro2[2]:
            ro1, ro2 = ro2, ro1
        r1 = ro1[2]
        r2 = ro2[2]
        d = distance(data)
        if d >= r1 + r2:
            return 0
        elif d <= r1 - r2:
            return pi * r2**2
        else:
            # 余弦定理：a^2 = b^2 + c^2 - 2*b*c*cosA
            cos1 = (r1**2 + d**2 - r2**2) / (2 * r1 * d)
            cos2 = (r2**2 + d**2 - r1**2) / (2 * r2 * d)
            sin1 = sqrt(1 - cos1**2)
            angle1 = 2 * degrees(acos(cos1))
            angle2 = 2 * degrees(acos(cos2))
            # 三角形面积： S = a * b * sinC / 2
            return round(
                (pi * (r1**2 * angle1 + r2**2 * angle2) / 360 - r1 * d * sin1),
                2)

    def is_swallow(data):
        ro1, ro2 = data
        if ro1[2] < ro2[2]:
            ro1, ro2 = ro2, ro1
        r1 = ro1[2]
        r2 = ro2[2]
        s1 = pi * r1**2
        s2 = pi * r2**2
        return True if s1 >= s2 * 1.2 and intersection_area(
            data) / s2 >= 0.55 else False

    def swallow(data):
        ro1, ro2 = data
        if ro1[2] < ro2[2]:
            ro1, ro2 = ro2, ro1
        r1 = ro1[2]
        r2 = ro2[2]
        s1 = pi * r1**2
        s2 = pi * r2**2
        r = round(sqrt((s1 + s2) / pi), 2)
        return (ro1[0], ro1[1], r)

    def sort_holes(data):
        temp = dict()
        for t in combinations(data, 2):
            d = distance(t)
            temp[d] = t
        temp = sorted(temp.items(), key=lambda d: d[0])
        rst = []
        for t in temp:
            rst.append(t[1])
        return rst

    while any([is_swallow(d) for d in combinations(data, 2)]):
        temp = sort_holes(data)
        for t in temp:
            if is_swallow(t):
                ro1, ro2 = t
                if ro1[2] < ro2[2]:
                    ro1, ro2 = ro2, ro1
                data.remove(ro2)
                n = data.index(ro1)
                data.remove(ro1)
                data.insert(n, swallow(t))
                break
    return data


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([(2, 4, 2), (3, 9, 3)]) == [(2, 4, 2), (3, 9, 3)]
    assert checkio([(0, 0, 2), (-1, 0, 2)]) == [(0, 0, 2), (-1, 0, 2)]
    assert checkio([(4, 3, 2), (2.5, 3.5, 1.4)]) == [(4, 3, 2.44)]
    assert checkio([(3, 3, 3), (2, 2, 1), (3, 5, 1.5)]) == [(3, 3, 3.5)]
