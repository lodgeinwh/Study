# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: 001.Multiples of 3 and 5.py
# @time: 2019/03/14 21:50:36
# @contact: lodgeinwh@gmail.com
# @version: 1.0

sums = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        sums += i
print(sums)
