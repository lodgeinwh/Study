# !/usr/bin/env python3
# -*- coding: utf-8 -*-


N = 600851475143
prime_factors = [1]
while N % 2 == 0:
    prime_factors.append(2)
    N = N // 2
while N % 3 == 0:
    prime_factors.append(3)
    N = N // 3
primes = [2, 3]
while max(prime_factors) < N:
    for i in range(max(primes), N+1, 2):
        if all([i % j for j in primes]):
            primes.append(i)
            if N % i == 0:
                prime_factors.append(i)
                N = N // i
                break
print(max(prime_factors[1:]))
