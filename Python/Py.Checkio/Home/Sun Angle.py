#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: lodgeinwh
# @license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
# @contact: lodgeinwh@gmail.com
# @file: Sun Angle.py
# @time: 2018-11-18 17:58


def sun_angle(time):
    hour, minute = map(int, time.split(':'))
    if 6 <= hour < 18:
        result = 180 / 12 * (hour - 6) + minute * 180 / 12 / 60
    elif hour == 18 and minute == 0:
        result = 180
    else:
        result = "I don't see the sun!"
    return result


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
