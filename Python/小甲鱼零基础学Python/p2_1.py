# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: p2_1.py
# @time: 2019/03/14 22:48:28
# @contact: lodgeinwh@gmail.com
# @version: 1.0


"""---第一个小游戏---"""
temp = input("不妨猜一下我现在心里想的数字：")
guess = int(temp)
if guess == 8:
    print("你是我心里的蛔虫吗？")
    print("猜中了也没奖！")
else:
    print("猜错了，我想的是数字8！")
print("游戏结束！")
