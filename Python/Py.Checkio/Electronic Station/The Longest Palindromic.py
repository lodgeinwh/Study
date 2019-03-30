# !/usr/bin/env python3
# -*- encoding: utf-8 -*-
# @Author: lodge
# @Contact: lodgeinwh@gmail.com
# @File: The Longest Palindromic.py
# @Time: 2019/1/31 22:18
# @Software: PyCharm


def longest_palindromic(text):
    l = len(text)
    for i in range(l):
        for j in range(i+1):
            if text[j: l-i+j] == text[j: l-i+j][::-1]:
                return text[j: l-i+j]


if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
