# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: 007.10001st prime.py
# @time: 2019/03/14 21:51:22
# @contact: lodgeinwh@gmail.com
# @version: 1.0


primes = [2]
i = 3
while len(primes) < 10001:
    if all(i % p != 0 for p in primes):
        primes.append(i)
    i += 2

print(primes[-1])
