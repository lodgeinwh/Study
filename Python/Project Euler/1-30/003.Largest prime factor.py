# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: 003.Largest prime factor.py
# @time: 2019/03/14 21:50:50
# @contact: lodgeinwh@gmail.com
# @version: 1.0


def primes(N):
    prime = []
    flag = [1] * (N + 2)
    p = 2
    while p <= N:
        prime.append(p)
        for i in range(2 * p, N + 1, p):
            flag[i] = 0
        while True:
            p += 1
            if flag[p] == 1:
                break
    return prime


import math

list = []


def prime_factors(n):
    isZhishu = True
    i = 2
    square = int(math.sqrt(n)) + 1
    while i <= square:
        if n % i == 0:
            list.append(i)
            isZhishu = False
            prime_factors(n // i)
            i += 1
            break
        i += 1
    if isZhishu:
        list.append(n)
    return list


n = 600851475143
print(prime_factors(n))
print(prime_factors(23456))
