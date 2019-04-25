#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: lodge
# @license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
# @contact: lodgeinwh@gmail.com
# @file: Boolean Algebra.py
# @time: 2018/12/29 22:34


OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")


def boolean(x, y, operation):
    if operation == "conjunction":
        if x == y == 1:
            return 1
        else:
            return 0

    if operation == "disjunction":
        if x == y == 0:
            return 0
        else:
            return 1

    if operation == "implication":
        if x == 0:
            return 1
        if x == 1:
            return y

    if operation == "exclusive":
        if x == y:
            return 0
        else:
            return 1

    if operation == "equivalence":
        if x == y:
            return 1
        else:
            return 0


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"
