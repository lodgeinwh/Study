# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: Double Substring.py
# @time: 2019/04/24 14:17:16
# @contact: lodgeinwh@gmail.com
# @version: 1.0


def double_substring(line):
    """
        length of the longest substring that non-overlapping repeats more than once.
    """
    l = len(line)
    if l == 2 and line[0] == line[1]:
        return 1
    for i in range(l - 2, 0, -1):
        for j in range(l - i):
            if line.count(line[j: j + i]) > 1:
                return i
    return 0


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert double_substring('aaaa') == 2, "First"
    assert double_substring('abc') == 0, "Second"
    assert double_substring('aghtfghkofgh') == 3, "Third"
    print('"Run" is good. How is "Check"?')
