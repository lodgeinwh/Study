# !/usr/bin/env python3
# -*- encoding: utf-8 -*-
# @Author: Lodge
# @Contact: lodgeinwh@gmail.com
# @File: Multicolored Lamp.py
# @Time: 2019/02/16 21:16:30


class Lamp:
    def __init__(self):
        self.color = ['Green', 'Red', 'Blue', 'Yellow']
        self.pos = -1

    def light(self):
        self.pos = (self.pos + 1) % len(self.color)
        return self.color[self.pos]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    lamp_1 = Lamp()
    lamp_2 = Lamp()

    lamp_1.light()  # Green
    lamp_1.light()  # Red
    lamp_2.light()  # Green

    assert lamp_1.light() == "Blue"
    assert lamp_1.light() == "Yellow"
    assert lamp_1.light() == "Green"
    assert lamp_2.light() == "Red"
    assert lamp_2.light() == "Blue"
    print("Coding complete? Let's try tests!")
