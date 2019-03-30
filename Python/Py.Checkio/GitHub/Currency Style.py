# !/usr/bin/env python3
# -*- encoding: utf-8 -*-
# @Author: lodge
# @Contact: lodgeinwh@gmail.com
# @File: Currency Style.py
# @Time: 2019/2/25 19:49
# @Software: PyCharm


def checkio(text):
    def trans(line):
        if line.count('.') == 0 and line.count(',') == 0:
            return line
        transtab = str.maketrans(',.', '.,')
        if line[-4] == '.' or ',' in line[-3:]:
            return line.translate(transtab)
        else:
            return line

    text = text.split(' ')
    res = []
    for t in text:
        if not t.startswith('$'):
            res.append(t)
        else:
            n = len(t)
            if t[-1].isdecimal():
                res.append(trans(t))
                continue
            else:
                for i in range(n - 1, 0, -1):
                    if t[i].isdecimal():
                        temp1 = t[:i + 1]
                        temp2 = t[i + 1:]
                        res.append(trans(temp1) + temp2)
                        break
    return ' '.join(res)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("$1.234.567,89") == "$1,234,567.89", "1st Example"
    assert checkio("$0,89") == "$0.89", "2nd Example"
    assert checkio("Euro Style = $12.345,67, US Style = $12,345.67") == "Euro Style = $12,345.67, US Style = $12,345.67", "European and US"
    assert checkio("Us Style = $12,345.67, Euro Style = $12.345,67") == "Us Style = $12,345.67, Euro Style = $12,345.67", "US and European"
    assert checkio("$1.234, $5.678 and $9") == "$1,234, $5,678 and $9", "Dollars without cents"
