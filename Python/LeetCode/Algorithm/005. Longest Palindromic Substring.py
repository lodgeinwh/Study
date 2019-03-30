# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: 005.Longest Palindromic Substring.py
# @time: 2019/02/26 20:32:14
# @contact: lodgeinwh@gmail.com
# @version: 1.0


class Solution:
    def longestPalindrome(self, s: 'str') -> 'str':
        n = len(s)
        if n == 0:
            return ''
        elif n == 1:
            return s
        else:
            for i in range(n, 0, -1):
                for j in range(n - i + 1):
                    if s[j:i + j] == s[j:i + j][::-1]:
                        return s[j:i + j]
        return s[0]
