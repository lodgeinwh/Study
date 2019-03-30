# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: 006.Sum square difference.py
# @time: 2019/03/14 21:51:14
# @contact: lodgeinwh@gmail.com
# @version: 1.0


sums = 0
sums_of_the_squares = 0
for i in range(1, 101):
    sums_of_the_squares += i ** 2
    sums += i

print(sums ** 2 - sums_of_the_squares)
