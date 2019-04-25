# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: Three Points Circle
# @time: 2019-02-01 9:53
# @contact: lodgeinwh@gmail.com


def checkio(data):
    (x1, y1) = eval(data[0:5])
    (x2, y2) = eval(data[6:11])
    (x3, y3) = eval(data[12:17])
    a = x1 - x2
    b = y1 - y2
    c = x1 - x3
    d = y1 - y3
    e = ((x1 ** 2 - x2 ** 2) - (y2 ** 2 - y1 ** 2)) / 2
    f = ((x1 ** 2 - x3 ** 2) - (y3 ** 2 - y1 ** 2)) / 2
    x0 = (d * e - b * f) / (a * d - b * c)
    y0 = (a * f - c * e) / (a * d - b * c)
    r = (((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5)
    f = lambda x: str(round(x, 2)).rstrip('0').rstrip('.')
    result = map(f, [x0, y0, r])
    return '(x-{})^2+(y-{})^2={}^2'.format(*result)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
