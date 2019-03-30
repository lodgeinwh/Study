# !/usr/bin/env python3
# -*- encoding: utf-8 -*-
# @Author: lodge
# @Contact: lodgeinwh@gmail.com
# @File: Number Factory.py
# @Time: 2019/2/1 14:16
# @Software: PyCharm


def checkio(number):
    result = ''
    for p in range(9, 1, -1):
        while not number % p:
            number //= p
            result = str(p) + result
    return int(result) if number == 1 else 0


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"
    assert checkio(1680) == 5678, "7th example"
    assert checkio(8146) == 0, "8th example"
    print('OK!')
