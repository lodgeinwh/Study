#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: lodge
# @contact: lodgeinwh@gmail.com
# @file: study.py
# @time: 2019/1/24 20:29

from abc import ABCMeta, abstractmethod

# ----------abstractfactory----------


class AbsCook(metaclass=ABCMeta):
    @abstractmethod
    def add_food(self, food_amount, food_price):
        pass

    @abstractmethod
    def add_drink(self, drink_amout, drink_price):
        pass

    @abstractmethod
    def total(self):
        pass
# ----------definitefactory----------


class JapaneseCook(AbsCook):
    def add_food(self, food_amount, food_price):
        pass

    def add_drink(self, food_amount, food_price):
        pass

    def total(self):
        pass


class RussianCook(AbsCook):
    def add_food(self, food_amount, food_price):
        pass

    def add_drink(self, food_amount, food_price):
        pass

    def total(self):
        pass


class ItalianCook(AbsCook):
    def add_food(self, food_amount, food_price):
        pass

    def add_drink(self, food_amount, food_price):
        pass

    def total(self):
        pass
# ----------abstractproduct----------


class AbsFood(metaclass=ABCMeta):
    @abstractmethod
    def create_food(self, food_amount, food_price):
        food_bill = food_amount * food_price
        return food_bill


class AbsDrink(metaclass=ABCMeta):
    @abstractmethod
    def create_drink(self, drink_amout, drink_price):
        drink_bill = drink_amout * drink_price
        return drink_bill
# ----------definiteproduct----------


class Sushi(AbsFood):
    def create_food(self, food_amount, food_price):
        return self.create_food()


class Tea(AbsDrink):
    def create_drink(self, drink_amout, drink_price):
        return self.create_drink()


class Dumpling(AbsFood):
    def create_food(self, food_amount, food_price):
        return self.create_food()


class Compute(AbsDrink):
    def create_drink(self, drink_amout, drink_price):
        return self.create_drink()


class Pizza(AbsFood):
    def create_food(self, food_amount, food_price):
        return self.create_food()


class Juice(AbsDrink):
    def create_drink(self, drink_amout, drink_price):
        return self.create_drink()


