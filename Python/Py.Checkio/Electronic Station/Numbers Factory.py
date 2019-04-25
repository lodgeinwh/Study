# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: Numbers Factory
# @time: 2019-02-01 9:56
# @contact: lodgeinwh@gmail.com


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


def checkio(number):
    factors = []
    while number >= 10:
        for p in range(9, 1, -1):
            if number % p == 0:
                factors.append(p)
                number //= p
                break
        if primes(number)[-1] == number and number > 10:
            return 0
    factors.append(number)

    result = ''
    for i in sorted(factors):
        if i > 10:
            return 0
        else:
            result += str(i)
    return int(result)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"
    assert checkio(8146) == 0, "7th example"
