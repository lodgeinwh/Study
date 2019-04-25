#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: lodge
# @license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
# @contact: lodgeinwh@gmail.com
# @file: Conversion into CamelCase.py
# @time: 2019/1/3 22:38


def to_camel_case(name):
    name_list = []
    for i in name.split('_'):
        name_list.append(i.title())
    return ''.join(name_list)


if __name__ == '__main__':
    print("Example:")
    print(to_camel_case('name'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_camel_case("my_function_name") == "MyFunctionName"
    assert to_camel_case("i_phone") == "IPhone"
    assert to_camel_case("this_function_is_empty") == "ThisFunctionIsEmpty"
    assert to_camel_case("name") == "Name"
    print("Coding complete? Click 'Check' to earn cool rewards!")
