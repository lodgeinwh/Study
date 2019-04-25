# !/usr/bin/env python3
# -*- coding: utf-8 -*-


primes = [2]
i = 3
while len(primes) < 10001:
    if all(i % p != 0 for p in primes):
        primes.append(i)
    i += 2


print(primes[-1])
