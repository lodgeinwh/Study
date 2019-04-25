#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: The Longest Palindromic
# @time: 2019-02-01 9:53
# @contact: lodgeinwh@gmail.com


def longest_palindromic(text):
    l = len(text)
    for i in range(l):
        for j in range(i + 1):
            if text[j: l - i + j] == text[j: l - i + j][::-1]:
                return text[j: l - i + j]


if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
