# !/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: Lodgeinwh
# @file: Stried Words.py
# @time: 2019/04/25 23:30:40
# @contact: lodgeinwh@gmail.com
# @version: 1.0


VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    import string
    text = text.upper()
    for i in text:
        if i in string.punctuation:
            text = text.replace(i, ' ')
        elif i in VOWELS:
            text = text.replace(i, 'v')
        elif i in CONSONANTS:
            text = text.replace(i, 'c')
    text = text.strip().split()

    result = 0
    for num_str in text:
        if len(num_str) > 1 and num_str.isalpha():
            if num_str.find('cc') == -1 and num_str.find('vv') == -1:
                result += 1
    return result


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
