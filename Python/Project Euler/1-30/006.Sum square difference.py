# !/usr/bin/env python3
# -*- coding: utf-8 -*-


sums = 0
sums_of_the_squares = 0
for i in range(1, 101):
    sums_of_the_squares += i ** 2
    sums += i

print(sums ** 2 - sums_of_the_squares)
