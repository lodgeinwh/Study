# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: 202. Happy Number.py
# @time: 2019/02/26 20:37:37
# @contact: lodgeinwh@gmail.com
# @version: 1.0


class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        d = {}
        while True:
            l = list(map(int, list(str(n))))
            m = 0
            for i in l:
                m += i**2
            if m in d:
                return False
            if m == 1:
                return True
            d[m] = m
            n = m
