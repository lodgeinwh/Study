# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: Parity Bit Generator.py
# @time: 2019/02/27 23:01:11
# @contact: lodgeinwh@gmail.com
# @version: 1.0


def checkio(message):
    rst = ''
    for i in message:
        m = str(bin(i))[2:-1]
        n = str(bin(i))[-1]
        if sum(map(lambda x: int(x), list(m))) % 2 == int(n):
            rst += chr(int(m, base=2))
    return rst


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([135, 134, 124, 233,
                    209, 81, 42, 202,
                    198, 194, 229, 215,
                    230, 146, 28, 210,
                    145, 137, 222, 158,
                    49, 81, 214, 157]) == "Checkio"
    assert checkio([144, 100, 200, 202,
                    216, 152, 164, 88,
                    216, 222, 65, 218,
                    175, 217, 248, 222,
                    171, 228, 216, 205,
                    254, 201, 193, 220]) == "Hello World"
