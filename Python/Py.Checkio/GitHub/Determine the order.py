# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: Determine the order.py
# @time: 2019/03/26 19:30:18
# @contact: lodgeinwh@gmail.com
# @version: 1.0


def checkio(data):
    import itertools

    def concatenate(word1, word2):
        if word1[-1] == word2[0]:
            return word1 + word2[1:]

    def repeat(word):
        res = ''
        for i in word:
            if i not in res:
                res += i
        return res

    def paste(word1, word2):
        if word2[0] in word1 and word2[-1] in word2:
            word1.replace(word2[0] + word2[-1], word2)
        return word1

    words = []
    for word in data:
        words.append(repeat(word))
    words = itertools.permutations()
    return ""


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(["acb", "bd", "zwa"]) == "zwacbd", \
        "Just concatenate it"
    assert checkio(["klm", "kadl", "lsm"]) == "kadlsm", \
        "Paste in"
    assert checkio(["a", "b", "c"]) == "abc", \
        "Cant determine the order - use english alphabet"
    assert checkio(["aazzss"]) == "azs", \
        "Each symbol only once"
    assert checkio(["dfg", "frt", "tyg"]) == "dfrtyg", \
        "Concatenate and paste in"
