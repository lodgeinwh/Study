# !/usr/bin/env python3
# -*- encoding: utf-8 -*-
# @Author: lodge
# @Contact: lodgeinwh@gmail.com
# @File: Time Converter (24h to 12h).py
# @Time: 2019/2/12 20:23
# @Software: PyCharm


def time_converter(time):
    time_s = time.split(':')
    if int(time_s[0]) == 0:
        return str(int(time_s[0]) + 12) + ':' + time_s[1] + ' a.m.'
    elif int(time_s[0]) < 12:
        return str(int(time_s[0])) + ':' + time_s[1] + ' a.m.'
    elif int(time_s[0]) == 12:
        return time + ' p.m.'
    else:
        return str(int(time_s[0]) - 12) + ':' + time_s[1] + ' p.m.'


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
