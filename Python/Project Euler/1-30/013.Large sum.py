#!/usr/bin/env python
# -*- encoding: UTF-8 -*-
# @File : 013.Large sum.py
# @Time : 2020/05/07 23:25:24
# @Author : Lodgeinwh
# @Contact : Lodgeinwh@gmail.com
# @Version : 1.0

matrix = 0
for line in open('pe13.txt').readlines():
    matrix += int(line)

print(int(str(matrix)[:10]))
