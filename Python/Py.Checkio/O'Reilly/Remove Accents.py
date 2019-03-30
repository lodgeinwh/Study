# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: lodge
# @license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
# @contact: lodgeinwh@gmail.com
# @file: Remove Accents.py
# @time: 2018/12/30 0:52


import unicodedata


def checkio(in_string):
    return ''.join(c for c in unicodedata.normalize('NFD', in_string) if unicodedata.category(c) != 'Mn')


if __name__ == '__main__':
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"
    print('Done')
