# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: 002.Even Fibonacci numbers.py
# @time: 2019/03/14 21:50:43
# @contact: lodgeinwh@gmail.com
# @version: 1.0


def fibonacci(L):
    fib = [1, 2]
    while fib[-1] + fib[-2] < L:
        fib.append(fib[-1] + fib[-2])
    return fib


sums = 0
for i in fibonacci(4000000):
    if i % 2 == 0:
        sums += i
print(sums)
