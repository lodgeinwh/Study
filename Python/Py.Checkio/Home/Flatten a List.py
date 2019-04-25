# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: Flatten a List.py
# @time: 2019/04/19 13:53:54
# @contact: lodgeinwh@gmail.com
# @version: 1.0


def flat_list(array):
    result = []
    for i in array:
        if isinstance(i, list):
            result.extend(flat_list(i))
        else:
            result.append(i)
    return result


if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6],
                              7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')
