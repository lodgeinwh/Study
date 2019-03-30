# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: 009.Special Pythagorean triplet.py
# @time: 2019/03/14 21:51:39
# @contact: lodgeinwh@gmail.com
# @version: 1.0


for a in range(1, 1000):  # 穷举法
    for b in range(a + 1, 1000):
        c = 1000 - a - b
        if a ** 2 + b ** 2 == c ** 2:
            print(a, b, c, a * b * c)
