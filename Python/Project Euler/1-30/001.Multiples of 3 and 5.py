# !/usr/bin/env python3
# -*- coding: utf-8 -*-

sums = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        sums += i
print(sums)
