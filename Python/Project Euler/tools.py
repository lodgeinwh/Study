#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def is_primes(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True


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
    prime_factor = []
    for p in primes(int(n ** 0.5) + 1):
        if n % p == 0:
            prime_factor.append(p)
    return prime_factor