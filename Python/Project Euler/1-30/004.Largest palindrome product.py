#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def palindrome(n):
    n = str(n)
    if n == n[::-1]:
        return True
    else:
        return False


palindromes = []
for a in range(100, 1000):
    for b in range(100, 1000):
        if palindrome(a * b):
            palindromes.append(a * b)
print(max(palindromes))
