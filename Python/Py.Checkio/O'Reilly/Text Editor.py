# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: lodge
# @license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
# @contact: lodgeinwh@gmail.com
# @file: Text Editor.py
# @time: 2018/12/29 23:01


class Text:
    def __init__(self, text='', font=''):
        self.text = text
        self.font = font

    def write(self, text):
        self.text += text

    def set_font(self, font):
        self.font = font

    def restore(self, get_version):
        self.text = get_version[0]
        self.font = get_version[1]

    def show(self):
        return '[{0}]{1}[{0}]'.format(self.font, self.text) if self.font else self.text


class SavedText:
    def __init__(self):
        self.texts = []
        self.fonts = []

    def save_text(self, text):
        self.texts.append(text.text)
        self.fonts.append(text.font)

    def get_version(self, number):
        return [self.texts[number], self.fonts[number]]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    text = Text()
    saver = SavedText()

    text.write("At the very beginning ")
    saver.save_text(text)
    text.set_font("Arial")
    saver.save_text(text)
    text.write("there was nothing.")

    assert text.show() == "[Arial]At the very beginning there was nothing.[Arial]"

    text.restore(saver.get_version(0))
    assert text.show() == "At the very beginning "

    print("Coding complete? Let's try tests!")
