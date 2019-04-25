# !/usr/bin/env python3
# -*- encoding: utf-8 -*-
# @Author: Lodge
# @Contact: lodgeinwh@gmail.com
# @File: Time Converter (12h to 24h).py
# @Time: 2019/02/16 19:21:49


def time_converter(time):
    # replace this for solution
    daytime = time.split(' ')[0].split(':')
    daynoon = time.split(' ')[1]
    if daytime[0] == '12' and daynoon == 'a.m.':
        return '00:00'
    if daytime[0] == '12' and daynoon == 'p.m.':
        return time.split(' ')[0]
    if daynoon == 'p.m.':
        return str(int(daytime[0]) + 12).rjust(2, '0') + ':' + daytime[1]
    if daynoon == 'a.m.':
        return str(int(daytime[0])).rjust(2, '0') + ':' + daytime[1]


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30 p.m.'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30 p.m.') == '12:30'
    assert time_converter('9:00 a.m.') == '09:00'
    assert time_converter('11:15 p.m.') == '23:15'
    print("Coding complete? Click 'Check' to earn cool rewards!")
