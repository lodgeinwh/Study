# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: lodge
# @license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
# @contact: lodgeinwh@gmail.com
# @file: 3 Chefs.py
# @time: 2019/1/9 23:28


# ------AbstractFactory------
class AbsFactory():
    food = None
    drink = None

    def __init__(self):
        self.food_bill = 0
        self.drink_bill = 0

    def add_food(self, food_amount, food_price):
        self.food_bill += food_amount * food_price

    def add_drink(self, drink_amount, drink_price):
        self.drink_bill += drink_amount * drink_price

    def total(self):
        return '{}: {}, {}: {}, Total: {}'.format(self.food, self.food_bill, self.drink, self.drink_bill, self.food_bill + self.drink_bill)


# ------DefiniteFactory------
class JapaneseCook(AbsFactory):
    food = 'Sushi'
    drink = 'Tea'


class ItalianCook(AbsFactory):
    food = 'Pizza'
    drink = 'Juice'


class RussianCook(AbsFactory):
    food = 'Dumplings'
    drink = 'Compote'


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    client_1 = JapaneseCook()
    client_1.add_food(2, 30)
    client_1.add_food(3, 15)
    client_1.add_drink(2, 10)

    client_2 = RussianCook()
    client_2.add_food(1, 40)
    client_2.add_food(2, 25)
    client_2.add_drink(5, 20)

    client_3 = ItalianCook()
    client_3.add_food(2, 20)
    client_3.add_food(2, 30)
    client_3.add_drink(2, 10)

    # print(client_1.total())
    assert client_1.total() == "Sushi: 105, Tea: 20, Total: 125"
    # print(client_2.total())
    assert client_2.total() == "Dumplings: 90, Compote: 100, Total: 190"
    # print(client_3.total())
    assert client_3.total() == "Pizza: 100, Juice: 20, Total: 120"
    print("Coding complete? Let's try tests!")
