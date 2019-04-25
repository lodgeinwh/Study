# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: Brackets.py
# @time: 2019/01/31 16:54:27
# @contact: lodgeinwh@gmail.com
# @version: 1.0


def checkio(expression):
    brackets_moudle = r'{}[]()'
    brackets_str = ''
    for i in expression:
        if i in brackets_moudle:
            brackets_str += i

    bra_len = len(brackets_str)
    if bra_len % 2 == 1:
        return False
    elif bra_len == 0:
        return True

    while True:
        if '()' in brackets_str:
            brackets_str = brackets_str.replace('()', '')
        elif '[]' in brackets_str:
            brackets_str = brackets_str.replace('[]', '')
        elif r'{}' in brackets_str:
            brackets_str = brackets_str.replace(r'{}', '')
        else:
            break

    return True if brackets_str == '' else False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
