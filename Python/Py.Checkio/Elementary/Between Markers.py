#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: lodge
# @license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
# @contact: lodgeinwh@gmail.com
# @file: Between Markers.py
# @time: 2018/12/24 23:15


def between_markers(text: str, begin: str, end: str) -> str:
    begin_index = text.find(begin)
    begin_len = len(begin)
    end_index = text.find(end)
    if begin_index == -1 and end_index == -1:
        return text
    elif begin_index == -1:
        text = text[:end_index]
    elif end_index == -1:
        text = text[begin_index + begin_len:]
    elif begin_index < end_index:
        text = text[begin_index + begin_len:end_index]
    else:
        text = ''
    return text


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
