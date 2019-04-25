# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: Call to Home.py
# @time: 2019/04/24 10:54:04
# @contact: lodgeinwh@gmail.com
# @version: 1.0


def total_cost(calls):
    from math import ceil
    list_calls = []
    for call in calls:
        list_calls.append(call.split(' '))
    dict_calls = {}
    for call in list_calls:
        if call[0] not in dict_calls:
            dict_calls[call[0]] = ceil(int(call[2]) / 60)
        else:
            dict_calls[call[0]] += ceil(int(call[2]) / 60)
    result = 0
    for v in dict_calls.values():
        if v <= 100:
            result += v
        else:
            result += 100 + 2 * (v - 100)
    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert total_cost(("2014-01-01 01:12:13 181",
                       "2014-01-02 20:11:10 600",
                       "2014-01-03 01:12:13 6009",
                       "2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost(("2014-02-05 01:00:00 1",
                       "2014-02-05 02:00:00 1",
                       "2014-02-05 03:00:00 1",
                       "2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost(("2014-02-05 01:00:00 60",
                       "2014-02-05 02:00:00 60",
                       "2014-02-05 03:00:00 60",
                       "2014-02-05 04:00:00 6000")) == 106, "Precise calls"
