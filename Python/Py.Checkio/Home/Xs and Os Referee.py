#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: lodgeinwh
# @license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
# @contact: lodgeinwh@gmail.com
# @file: Xs and Os Referee.py
# @time: 2018-11-18 20:24


def checkio(game_result):
    for i in range(0, 3):
        if game_result[0][i] == game_result[1][i] == game_result[2][i] == 'X' or\
           game_result[i][0] == game_result[i][1] == game_result[i][2] == 'X' or\
           game_result[1][1] == game_result[0][0] == game_result[2][2] == 'X' or\
           game_result[1][1] == game_result[0][2] == game_result[2][0] == 'X' :
            return "X"
        elif game_result[0][i] == game_result[1][i] == game_result[2][i] == 'O' or\
             game_result[i][0] == game_result[i][1] == game_result[i][2] == 'O' or\
             game_result[1][1] == game_result[0][0] == game_result[2][2] == 'O' or\
             game_result[1][1] == game_result[0][2] == game_result[2][0] == 'O' :
            return "O"
    return "D"


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
