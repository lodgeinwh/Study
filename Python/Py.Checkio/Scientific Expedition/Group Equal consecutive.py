# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: Group Equal consecutive.py
# @time: 2019/04/24 16:11:10
# @contact: lodgeinwh@gmail.com
# @version: 1.0


def group_equal(els):
    l = len(els)
    if l == 0:
        return []
    elif l == 1:
        return [els]
    else:
        result = []
        temp = [els[0]]
        els.pop(0)
        while els:
            if els[0] in temp:
                temp.append(els[0])
                els.pop(0)
            else:
                result.append(temp)
                temp = [els[0]]
                els.pop(0)
        result.append(temp)
    return result


if __name__ == '__main__':
    print("Example:")
    print(group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert group_equal([1, 1, 4, 4, 4, "hello", "hello",
                        4]) == [[1, 1], [4, 4, 4], ["hello", "hello"], [4]]
    assert group_equal([1, 2, 3, 4]) == [[1], [2], [3], [4]]
    assert group_equal([1]) == [[1]]
    assert group_equal([]) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
