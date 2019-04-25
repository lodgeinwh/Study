# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: lodgeinwh
# @license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
# @contact: lodgeinwh@gmail.com
# @file: The Warriors.py
# @time: 2018-11-18 20:30


class Warrior():
    def __init__(self):
        self.health = 50
        self.damage = 5

    @property
    def is_alive(self):
        return self.health > 0

    def do_hit(self, enemy1):
        enemy1.health -= self.damage


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.damage = 7


def fight(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        unit_1.do_hit(unit_2)
        if not unit_2.is_alive:
            break
        unit_2.do_hit(unit_1)
        if not unit_1.is_alive:
            break
    return unit_1.is_alive


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")
