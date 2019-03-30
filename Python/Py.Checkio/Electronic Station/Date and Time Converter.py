# !/usr/bin/env python3
# -*- encoding: utf-8 -*-
# @Author: Lodge
# @Contact: lodgeinwh@gmail.com
# @File: Date and Time Converter.py
# @Time: 2019/02/16 20:05:58


def date_time(time: str) -> str:
    # replace this for solution
    months = ['0', 'January', 'February', 'March', 'April', 'May', 'June', 'July',\
              'August', 'Septemper', 'October', 'November', 'December']
    day, month, year = map(int, time.split(' ')[0].split('.'))
    hour, minute = map(int, time.split(' ')[1].split(':'))
    month = months[month]
    return f"{day} {month} {year} year {hour} hour{'s' if hour != 1 else ''} {minute} minute{'s' if minute != 1 else ''}"


if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00"
                     ) == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time(
        "09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time(
        "20.11.1990 03:55"
    ) == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
