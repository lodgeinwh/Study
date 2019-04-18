# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: 007. Reverse Integer.py
# @time: 2019/04/09 23:45:16
# @contact: lodgeinwh@gmail.com
# @version: 1.0


class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            ans = int(str(x)[::-1])
        else:
            ans = int(str(-x)[::-1]) * -1

        if x > 2 ** 31 - 1 or x < -1 * 2 ** 31:
            return 0
        else:
            return ans
