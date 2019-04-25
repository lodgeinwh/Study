#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: lodge
# @license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
# @contact: lodgeinwh@gmail.com
# @file: The Most Frequent Weekdays.py
# @time: 2019/1/3 22:53


from calendar import isleap, weekday, day_name


def most_frequent_days(year):
    days = (weekday(year, 1, i+1) for i in range(1 + isleap(year)))
    return [day_name[d] for d in sorted(days)]


'''
def most_frequent_days(year):
    import datetime
    import calendar
    result = []
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    weekday = datetime.datetime(year, month=1, day=1).weekday()
    if calendar.isleap(year):
        result.append(week[weekday])
        result.append(week[(weekday + 1) % 7])
    else:
        result.append(week[weekday])
    if result[-1] == 'Monday':
        result.reverse()
    return result
'''

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent_days(2399) == ['Friday'], "1st example"
    assert most_frequent_days(1152) == ['Tuesday', 'Wednesday'], "2nd example"
    assert most_frequent_days(56) == ['Saturday', 'Sunday'], "3rd example"
    assert most_frequent_days(2909) == ['Tuesday'], "4th example"
