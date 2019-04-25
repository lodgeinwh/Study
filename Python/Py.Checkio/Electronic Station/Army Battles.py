# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: Army Battles.py
# @time: 2019/04/22 13:25:44
# @contact: lodgeinwh@gmail.com
# @version: 1.0


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


class Army():
    def __init__(self,):
        self.army = []

    def add_units(self, soldier, number):
        for i in range(number):
            self.army.append(soldier())


class Battle():
    def fight(self, army_1, army_2):
        while army_1.army and army_2.army:
            if fight(army_1.army[0], army_2.army[0]):
                army_2.army.pop(0)
            else:
                army_1.army.pop(0)
        return True if army_1.army else False


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

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
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

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)
    
    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")
