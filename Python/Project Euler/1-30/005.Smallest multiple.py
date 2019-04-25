# !/usr/bin/env python3
# -*- coding: utf-8 -*-


def zdgys(x, y):  # 求最大公约数
    if x > y:
        x, y = y, x
    while y % x != 0:
        y, x = x, y % x
    return x


def zxgbs(x, y):
    return x * y // zdgys(x, y)


i = 2
result = 1
while i <= 20:
    result = zxgbs(result, i)
    i += 1

print(result)
