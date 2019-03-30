# !/usr/bin/env python3
# -*- encoding: utf-8 -*-
# @Author: lodge
# @Contact: lodgeinwh@gmail.com
# @File: 242. Valid Anagram.py
# @Time: 2019/2/26 20:40
# @Software: PyCharm


from collections import Counter


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        c1 = Counter(s)
        c2 = Counter(t)
        if (c1 == c2):
            return True
        return False
