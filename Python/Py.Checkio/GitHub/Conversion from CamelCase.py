# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: Conversion from CamelCase.py
# @time: 2019/02/26 21:16:51
# @contact: lodgeinwh@gmail.com
# @version: 1.0


'''
def from_camel_case(name):
    # replace this for solution
    rst = [name[0], ]
    n = len(name)
    for i in range(1, n):
        if name[i].isupper():
            rst.append('_')
            rst.append(name[i])
        else:
            rst.append(name[i])
    return ''.join(rst).lower()
'''


def from_camel_case(name):
    return ''.join(['_' + i.lower() if i.isupper() else i for i in name])[1:]


if __name__ == '__main__':
    print("Example:")
    print(from_camel_case("Name"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert from_camel_case("MyFunctionName") == "my_function_name"
    assert from_camel_case("IPhone") == "i_phone"
    assert from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
    assert from_camel_case("Name") == "name"
    print("Coding complete? Click 'Check' to earn cool rewards!")
