# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: Binary Count.py
# @time: 2019/03/26 19:35:55
# @contact: lodgeinwh@gmail.com
# @version: 1.0


def checkio(number):
    return str(bin(number))[2:].count('1')


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4) == 1
    assert checkio(15) == 4
    assert checkio(1) == 1
    assert checkio(1022) == 9
