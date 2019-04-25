# !/usr/bin/env python3
# -*- coding: utf-8 -*-


def primes(N):
    prime = []
    flag = [1] * (N+2)
    p = 2
    while p <= N:
        prime.append(p)
        for i in range(2*p, N+1, p):
            flag[i] = 0
        while True:
            p += 1
            if flag[p] == 1:
                break
    return prime

print(sum(primes(2000000)))
