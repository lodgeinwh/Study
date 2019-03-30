# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: lodge
# @contact: lodgeinwh@gmail.com
# @file: test.py
# @time: 2018/12/23 14:44

import itertools


d = ["acb", "bd", "zwa"]
b = True
while b:
    ts = itertools.permutations(d, 2)
    for t in ts:
        if t[0][-1] == t[1][0]:
            d.append(t[0] + t[1][1:])
            d.remove(t[0])
            d.remove(t[1])
            break

print(d)
