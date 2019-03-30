# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: Stried Words.py
# @time: 2019/03/14 22:15:20
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
    text = text.strip().split(' ')

    count = 0
    for s in text:
        if len(s) > 1 and s.isalpha():
            if s.find('vv') == -1 and s.find('cc') == -1:
                count += 1
    return count


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
