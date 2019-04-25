# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: lodgeinwh
# @license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
# @contact: lodgeinwh@gmail.com
# @file: Non-unique Elements.py
# @time: 2018-11-18 16:17


def checkio(data):
    mydata = []
    for j in data:
        if data.count(j) > 1:
            mydata.append(j)
    return mydata


'''
    return [i for i in data if data.count(i) > 1]
'''

# Some hints
# You can use list.count(element) method for counting.
# Create new list with non-unique elements
# Loop over original list


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")
