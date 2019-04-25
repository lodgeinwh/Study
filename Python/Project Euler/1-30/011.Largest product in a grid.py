#!/usr/bin/env python3
# -*- coding: utf-8 -*-


matrix = []
for line in open('pe11.txt').readlines():
    matrix.append(line.rstrip().split(' '))  # 读取数据


L = 4
product = [0] * 4
for i in range(len(matrix) - L + 1):
    for j in range(len(matrix[0]) - L + 1):
        product0, product1, product2 = 1, 1, 1
        for k in range(L):
            product0 *= int(matrix[i + k][j])  # 竖向乘积
            product1 *= int(matrix[i][j + k])  # 横向乘积
            product2 *= int(matrix[i + k][j + k])  # 斜向乘积
            if product0 > product[0]:
                product[0] = product0
            if product1 > product[1]:
                product[1] = product1
            if product2 > product[2]:
                product[2] = product2
for i in range(len(matrix) - L + 1):
    for j in range(L - 1, len(matrix[0])):
        product3 = 1
        for k in range(L):
            product3 *= int(matrix[i + k][j - k])  # 反斜向乘积
            if product3 > product[3]:
                product[3] = product3

print(max(product))
