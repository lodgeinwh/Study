#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: The Hamming Distance.py
# @time: 2019/01/31 16:29:53
# @contact: lodgeinwh@gmail.com
# @version: 1.0


def checkio(n, m):
    return bin(n ^ m).count('1')


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
