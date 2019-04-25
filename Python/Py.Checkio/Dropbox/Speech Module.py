# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: lodge
# @license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
# @contact: lodgeinwh@gmail.com
# @file: Speech Module.py
# @time: 2019/1/3 22:42


FIRST_TEN = ["zero", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    voice = ''
    if number >= 100:
        hundreds_digit = number // 100
        tens_single_digit = number % 100
        if tens_single_digit == 0:
            voice = FIRST_TEN[hundreds_digit] + ' ' + HUNDRED
        else:
            voice = FIRST_TEN[hundreds_digit] + ' ' + HUNDRED + ' ' + checkio(tens_single_digit)
    elif 100 > number >= 20:
        tens_digit = number // 10
        single_digit = number % 10
        if single_digit == 0:
            voice = OTHER_TENS[tens_digit - 2]
        else:
            voice = OTHER_TENS[tens_digit - 2] + ' ' + checkio(single_digit)
    elif 20 > number >= 10:
        voice = SECOND_TEN[number - 10]
    elif 10 > number >= 0:
        voice = FIRST_TEN[number]
    return voice


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
