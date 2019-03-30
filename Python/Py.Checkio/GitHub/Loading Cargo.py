# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: Loading Cargo.py
# @time: 2019/03/12 22:13:47
# @contact: lodgeinwh@gmail.com
# @version: 1.0


def checkio(data):  # 问题转化为在数组data中，找到一个子数组，是子数组的和最接近V
    import numpy as np
    n = len(data)
    halfsum = int(sum(data) / 2)
    dp = np.zeros((n + 1, halfsum + 1))
    value = data.copy()
    weight = data.copy()
    for i in range(1, n + 1):
        for j in range(1, halfsum + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= weight[i - 1] and dp[i][j] < dp[i - 1][
                    j - weight[i - 1]] + value[i - 1]:
                dp[i][j] = dp[i - 1][j - weight[i - 1]] + value[i - 1]
    return sum(data) - 2 * dp[-1][-1]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([10, 10]) == 0, "1st example"
    assert checkio([10]) == 10, "2nd example"
    assert checkio([5, 8, 13, 27, 14]) == 3, "3rd example"
    assert checkio([5, 5, 6, 5]) == 1, "4th example"
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, "5th example"
    assert checkio([1, 1, 1, 3]) == 0, "6th example"
