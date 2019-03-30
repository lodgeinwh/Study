# !/usr/bin/env python3
# -*- encoding: utf-8 -*-
# @Author: Lodge
# @Contact: lodgeinwh@gmail.com
# @File: Reverse Roman Numerals.py
# @Time: 2019/02/16 22:55:56


def reverse_roman(roman_string):
    # replace this for solution
    roman = {'CM': 900, 'M': 1000, 'CD': 400, 'D': 500, 'XC': 90, 'C': 100, 'XL': 40, 'L': 50, 'IX': 9, 'X': 10, 'IV': 4, 'V': 5, 'I': 1}
    result = 0
    while len(roman_string) != 0:
        for i in roman.keys():
            if i in roman_string:
                result += roman[i]
                roman_string = roman_string.replace(i, '', 1)
                break
    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    print('Great! It is time to Check your code!')
