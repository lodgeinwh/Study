# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: 003.3. Longest Substring Without Repeating Characters.py
# @time: 2019/02/26 20:20:14
# @contact: lodgeinwh@gmail.com
# @version: 1.0


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        import re

        r = []
        for i in range(len(s)):
            for j in range(i, len(s) + 1):
                if not re.search(r"(.).*\1", s[i:j]):
                    r.append(s[i:j])

        return len(s if len(s) < 2 else max(r, key=lambda x: len(x)))
