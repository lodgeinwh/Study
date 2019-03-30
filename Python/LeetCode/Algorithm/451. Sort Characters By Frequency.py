# !/usr/bin/env python3
# -*- encoding: utf-8 -*-
# @Author: lodge
# @Contact: lodgeinwh@gmail.com
# @File: 451. Sort Characters By Frequency.py
# @Time: 2019/2/26 20:42
# @Software: PyCharm


class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        d = Counter(s).most_common(len(s))
        res = []
        for i in d:
            res.extend([i[0] * i[1]])
        return ''.join(res)
