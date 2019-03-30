# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: 012.Highly divisible triangular number.py
# @time: 2019/03/14 21:52:04
# @contact: lodgeinwh@gmail.com
# @version: 1.0


def triangular_number(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


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


def prime_factors(n):
    from math import sqrt
    prime_factor = []
    for p in primes(int(sqrt(n)) + 1):
        if n % p == 0:
            prime_factor.append(p)
        return prime_factors(n // p)


print(primes(23456))
print(prime_factors(23456))
