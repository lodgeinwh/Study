# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: The Fastest Horse.py
# @time: 2019/04/25 13:29:57
# @contact: lodgeinwh@gmail.com
# @version: 1.0


def fastest_horse(horses: list) -> int:
    horse_dict = {}
    for i in range(len(horses[0])):
        horse_dict[i] = 0
    for race in horses:
        temp = []
        for time in race:
            temp.append(int(time.split(':')[0]) * 60 + int(time.split(':')[1]))
        horse_dict[temp.index(min(temp))] += 1
    return list(horse_dict.values()).index(max(horse_dict.values())) + 1


if __name__ == '__main__':
    print("Example:")
    print(fastest_horse([['1:13', '1:26', '1:11']]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert fastest_horse([['1:13', '1:26', '1:11'], ['1:10', '1:18', '1:14'], ['1:20', '1:23', '1:15']]) == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")
