#!/usr/bin/env python3
# -*- coding: utf-8 -*-


d = ''.join(line.rstrip() for line in open('pe8.txt'))
max_product = 0
L = 13
for i in range(len(d)-L):
    product = 1
    for j in range(L):
        product *= int(d[i+j])
    if product > max_product:
        max_product = product

print(max_product)
