# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: 005.Smallest multiple.py
# @time: 2019/03/14 21:51:03
# @contact: lodgeinwh@gmail.com
# @version: 1.0


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
