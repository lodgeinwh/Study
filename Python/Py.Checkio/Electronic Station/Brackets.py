# !/usr/bin/env python3
# -*- encoding: utf-8 -*-
# @Author: lodge
# @Contact: lodgeinwh@gmail.com
# @File: Brackets.py
# @Time: 2019/1/31 20:53
# @Software: PyCharm


def checkio(expression):
    brackets_str = r'{}[]()'
    brackets = ''
    for i in expression:
        if i in brackets_str:
            brackets += i

    bra_len = len(brackets)
    if bra_len % 2 == 1:
        return False
    elif bra_len == 0:
        return True

    while True:
        if '()' in brackets:
            brackets = brackets.replace('()', '')
        elif '[]' in brackets:
            brackets = brackets.replace('[]', '')
        elif '{}' in brackets:
            brackets = brackets.replace('{}', '')
        else:
            break

    return True if brackets == '' else False


if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
