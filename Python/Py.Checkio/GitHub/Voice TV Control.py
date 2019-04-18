# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: Voice TV Control.py
# @time: 2019/04/14 16:56:10
# @contact: lodgeinwh@gmail.com
# @version: 1.0


class VoiceCommand:
    def __init__(self, channels):
        self.channels = channels
        self.channel = self.channels[0]

    def first_channel(self):
        return self.channels[0]

    def last_channel(self):
        return self.channels[-1]

    def turn_channel(self, N):
        self.channel = self.channels[N - 1]
        return self.channel

    def next_channel(self):
        index = self.channels.index(self.channel)
        if index == len(self.channels) - 1:
            self.channel = self.channels[0]
        if index < len(self.channels) - 1:
            self.channel = self.channels[index + 1]
        return self.channel

    def previous_channel(self):
        index = self.channels.index(self.channel)
        if index == 0:
            self.channel = self.channels[-1]
        if index < len(self.channels) - 1:
            self.channel = self.channels[index - 1]
        return self.channel

    def current_channel(self):
        return self.channel

    def is_exist(self, m):
        if isinstance(m, int) and 0 < m < len(self.channels):
            return "Yes"
        elif isinstance(m, str) and m in self.channels:
            return "Yes"
        else:
            return "No"

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    CHANNELS = ["BBC", "Discovery", "TV1000"]

    controller = VoiceCommand(CHANNELS)
    
    assert controller.first_channel() == "BBC"
    assert controller.last_channel() == "TV1000"
    assert controller.turn_channel(1) == "BBC"
    assert controller.next_channel() == "Discovery"
    assert controller.previous_channel() == "BBC"
    assert controller.current_channel() == "BBC"
    assert controller.is_exist(4) == "No"
    assert controller.is_exist("TV1000") == "Yes"
    print("Coding complete? Let's try tests!")
