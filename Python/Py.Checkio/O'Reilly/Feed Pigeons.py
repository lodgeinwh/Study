# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: Feed Pigeons.py
# @time: 2019/03/14 22:08:46
# @contact: lodgeinwh@gmail.com
# @version: 1.0


def checkio(number):
    time = 0  # 初始时间
    pigeon = 0  # 初始鸽子数量
    while True:
        time += 1  # 实时时间
        pigeon += time  # 实时鸽子数量
        if number >= pigeon:  # 如果剩余粮食大于鸽子数量
            number -= pigeon  # 鸽子吃掉粮食
            continue
        else:
            return max(pigeon - time, number)  # 如果剩余粮食小于鸽子数量，那么吃到粮食的鸽子数量就是上一轮鸽子数量和剩余粮食中较大的一个


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
