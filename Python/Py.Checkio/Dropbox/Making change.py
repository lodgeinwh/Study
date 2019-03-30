# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: lodge
# @license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
# @contact: lodgeinwh@gmail.com
# @file: Making change.py
# @time: 2019/1/4 23:36


def checkio(price, denominations):
    coins_result = [set(denominations), set(denominations)]
    times = 1
    while price not in coins_result[-1]:
        coins_result.append(set())
        for i in list(coins_result[0]):
            for j in list(coins_result[times]):
                coins_result[-1].add(i + j)
        times += 1
        if price < min(coins_result[-1]):
            return None
    return times


'''def checkio(price, denominations):
    coins = []
    for i in range(price // min(denominations) + 1):
        coins.append(set())
    for j in denominations:
        coins[0].add(j)
        coins[1].add(j)
    k = 2
    while k < price // min(denominations):
        for m in coins[k - 2]:
            for n in coins[k - 1]:
                coins[k].add(m + n)
        if price in coins[k]:
            return k
        else:
            k += 1
    return None'''


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(8, [1, 3, 5]) == 2
    assert checkio(12, [1, 4, 5]) == 3
    assert checkio(123456, [1, 6, 7, 456, 678]) == 187
    assert checkio(4, [3, 5]) == None
    print('Done')
