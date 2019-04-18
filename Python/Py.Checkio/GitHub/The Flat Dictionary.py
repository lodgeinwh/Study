# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: The Flat Dictionary.py
# @time: 2019/04/14 11:57:52
# @contact: lodgeinwh@gmail.com
# @version: 1.0


'''def flatten(dictionary, path=[]):
    from collections import ChainMap
    if dictionary and isinstance(dictionary, dict):
        return dict(ChainMap(*(flatten(v, path + [k]) for k, v in dictionary.items())))
    return {"/".join(path): dictionary or ""}'''


def flatten(dictionary):
    check = [isinstance(dictionary[item], dict) for item in dictionary]
    if not any(check):
        return dictionary
    else:
        for k in list(dictionary):
            if isinstance(dictionary[k], dict):
                if not dictionary[k]:
                    dictionary[k] = ""
                else:
                    for v in dictionary[k]:
                        dictionary[k+'/'+v] = dictionary[k][v]
                    dictionary.pop(k)
    return flatten(dictionary)


if __name__ == '__main__':
    test_input = {"key": {"deeper": {"more": {"enough": "value"}}}}
    print(' Input: {}'.format(test_input))
    print('Output: {}'.format(flatten(test_input)))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({"name": {
                        "first": "One",
                        "last": "Drone"},
                    "job": "scout",
                    "recent": {},
                    "additional": {
                        "place": {
                            "zone": "1",
                            "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}
    print('You all set. Click "Check" now!')
