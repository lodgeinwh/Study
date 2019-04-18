# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: lodge
# @contact: lodgeinwh@gmail.com
# @file: test.py
# @time: 2018/12/23 14:44


class VoiceCommand:
    def __init__(self, channels):
        self.channels = channels
        self.index = 0

    def first_channel(self):
        return self.channels[self.index]

    def last_channel(self):
        self.index = len(self.channels) - 1
        return self.channels[-1]

    def turn_channel(self, N):
        self.index = N - 1
        return self.channels[self.index]

    def next_channel(self):
        self.index = (self.index + 1) % len(self.channels)
        return self.channels[self.index]

    def previous_channel(self):
        self.index -= 1
        return self.channels[self.index]

    def current_channel(self):
        return self.channels[self.index]

    def is_exist(self, m):
        if isinstance(m, int) and 0 < m < len(self.channels):
            return "Yes"
        elif isinstance(m, str) and m in self.channels:
            return "Yes"
        else:
            return "No"


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    CHANNELS = ['BBC', 'Discovery', 'NickMusic', 'MTV']

    controller = VoiceCommand(CHANNELS)

    controller.previous_channel()
    controller.previous_channel()
    print(controller.current_channel())
    print("Coding complete? Let's try tests!")
