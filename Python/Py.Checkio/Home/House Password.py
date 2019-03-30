#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: lodgeinwh
# @license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
# @contact: lodgeinwh@gmail.com
# @file: House Password.py
# @time: 2018-11-18 16:07


def checkio(data):
    result1 = all(char.isalnum() for char in data)
    result2 = any(char.isdigit() for char in data)
    result3 = any(char.isupper() for char in data)
    result4 = any(char.islower() for char in data)
    result5 = True if len(data) >= 10 else False
    result = result1 and result2 and result3 and result4 and result5
    return result


# Some hints
# Just check all conditions

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print(
        "Coding complete? Click 'Check' to review your tests and earn cool rewards!"
    )
