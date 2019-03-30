# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: p4_5.py
# @time: 2019/03/14 22:49:34
# @contact: lodgeinwh@gmail.com
# @version: 1.0


for i in range(10):
    if i % 2 != 0:
        print(i)
        continue
    i += 2
    print(i)
