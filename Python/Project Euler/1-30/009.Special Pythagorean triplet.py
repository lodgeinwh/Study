# !/usr/bin/env python3
# -*- coding: utf-8 -*-


for a in range(1, 1000): # 穷举法
    for b in range(a + 1, 1000):
        c = 1000 - a - b
        if a ** 2 + b ** 2 == c ** 2:
            print(a, b, c, a * b * c)
