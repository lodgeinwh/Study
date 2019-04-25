#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: lodge
# @license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
# @contact: lodgeinwh@gmail.com
# @file: Inside Block.py
# @time: 2019/1/10 21:40


def cross(s_point, e_point, t_point):
    if s_point[1] != e_point[1]:
        x = s_point[0] + (t_point[1] - s_point[1]) * (e_point[0] - s_point[0]) / (e_point[1] - s_point[1])
        if x >= t_point[0] and (s_point[1] >= t_point[1] >= e_point[1] or s_point[1] <= t_point[1] <= e_point[1]):
            return x, t_point[1]


def is_inside(polygon, point):
    polygon_line = [[polygon[-1], polygon[0]]]
    for i in range(len(polygon) - 1):
        polygon_line.append([polygon[i], polygon[i + 1]])

    cross_set = set()
    for sp, ep in polygon_line:
        cross_set.add(cross(sp, ep, point))
    cross_set.remove(None)
    for p in cross_set:
        if p == point or p in polygon:
            return True
    if len(cross_set) % 2 == 1:
        return True
    else:
        return False


if __name__ == '__main__':
    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)),
                     (2, 2)) == True, "First"
    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)),
                     (4, 2)) == False, "Second"
    assert is_inside(((1, 1), (4, 1), (2, 3)),
                     (3, 2)) == True, "Third"
    assert is_inside(((1, 1), (4, 1), (1, 3)),
                     (3, 3)) == False, "Fourth"
    assert is_inside(((2, 1), (4, 1), (5, 3), (3, 4), (1, 3)),
                     (4, 3)) == True, "Fifth"
    assert is_inside(((2, 1), (4, 1), (3, 2), (3, 4), (1, 3)),
                     (4, 3)) == False, "Sixth"
    assert is_inside(((1, 1), (3, 2), (5, 1), (4, 3), (5, 5), (3, 4), (1, 5), (2, 3)),
                     (3, 3)) == True, "Seventh"
    assert is_inside(((1, 1), (1, 5), (5, 5), (5, 4), (2, 4), (2, 2), (5, 2), (5, 1)),
                     (4, 3)) == False, "Eighth"