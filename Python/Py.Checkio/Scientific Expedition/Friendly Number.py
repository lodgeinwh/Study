# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: Friendly Number.py
# @time: 2019/04/25 09:52:21
# @contact: lodgeinwh@gmail.com
# @version: 1.0


def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    value = abs(number)
    for n in range(len(powers)):
        if value / base ** n < base:
            break
    value = value / base ** n    
    if decimals:
        fomat_string =  '{:.%df}{}{}' % (decimals)
        result = fomat_string.format(value, powers[n], suffix)
    else:
        fomat_string = '{}{}{}'
        result = fomat_string.format(int(value), powers[n], suffix)
    return result if number >= 0 else '-' + result



# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'
    assert friendly_number(12000000, decimals=3) == '12.000M'
    assert friendly_number(-150, base=100, powers=["","d","D"]) == "-1d"
    assert friendly_number(255000000000, powers=["","k","M"])
