#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: lodge
# @license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
# @contact: lodgeinwh@gmail.com
# @file: Compare Functions.py
# @time: 2019/1/5 18:43


def checkio(f, g):
    def h(*args, **kwargs):
        try:
            f_out = f(*args, **kwargs)
        except:
            try:
                g_out = g(*args, **kwargs)
            except:
                return None, 'both_error'
            else:
                if g_out is None:
                    return None, 'both_error'
                else:
                    return g_out, 'f_error'
        else:
            if f_out is None:
                try:
                    g_out = g(*args, **kwargs)
                except:
                    return None, 'both_error'
                else:
                    if g_out is None:
                        return None, 'both_error'
                    else:
                        return g_out, 'f_error'
            else:
                try:
                    g_out = g(*args, **kwargs)
                except:
                    return f_out, 'g_error'
                else:
                    if g_out is None:
                        return f_out, 'g_error'
                    else:
                        if f_out == g_out:
                            return f_out, 'same'
                        else:
                            return f_out, 'different'

    return h


if __name__ == '__main__':

    # These "asserts" using only for self-checking and not necessary for auto-testing

    # (x+y)(x-y)/(x-y)
    assert checkio(lambda x, y: x + y,
                   lambda x, y: (x ** 2 - y ** 2) / (x - y))(1, 3) == (4, 'same'), "Function: x+y, first"
    assert checkio(lambda x, y: x + y,
                   lambda x, y: (x ** 2 - y ** 2) / (x - y))(1, 2) == (3, 'same'), "Function: x+y, second"
    assert checkio(lambda x, y: x + y,
                   lambda x, y: (x ** 2 - y ** 2) / (x - y))(1, 1.01) == (2.01, 'different'), "x+y, third"
    assert checkio(lambda x, y: x + y,
                   lambda x, y: (x ** 2 - y ** 2) / (x - y))(1, 1) == (2, 'g_error'), "x+y, fourth"

    # Remove odds from list
    f = lambda nums: [x for x in nums if ~x % 2]

    def g(nums):
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                nums.pop(i)
        return nums


    assert checkio(f, g)([2, 4, 6, 8]) == ([2, 4, 6, 8], 'same'), "evens, first"
    assert checkio(f, g)([2, 3, 4, 6, 8]) == ([2, 4, 6, 8], 'g_error'), "evens, second"

    # Fizz Buzz
    assert checkio(lambda n: ("Fizz " * (1 - n % 3) + "Buzz " * (1 - n % 5))[:-1] or str(n),
                   lambda n: ('Fizz' * (n % 3 == 0) + ' ' + 'Buzz' * (n % 5 == 0)).strip())(6) == ('Fizz', 'same'), \
        "fizz buzz, first"
    assert checkio(lambda n: ("Fizz " * (1 - n % 3) + "Buzz " * (1 - n % 5))[:-1] or str(n),
                   lambda n: ('Fizz' * (n % 3 == 0) + ' ' + 'Buzz' * (n % 5 == 0)).strip())(30) == (
           'Fizz Buzz', 'same'), \
        "fizz buzz, second"
    assert checkio(lambda n: ("Fizz " * (1 - n % 3) + "Buzz " * (1 - n % 5))[:-1] or str(n),
                   lambda n: ('Fizz' * (n % 3 == 0) + ' ' + 'Buzz' * (n % 5 == 0)).strip())(7) == ('7', 'different'), \
        "fizz buzz, third"
