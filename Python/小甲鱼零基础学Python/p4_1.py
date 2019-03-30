# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: p4_1.py
# @time: 2019/03/14 22:48:46
# @contact: lodgeinwh@gmail.com
# @version: 1.0


score = int(input("请输入一个分数："))
if 100 >= score >= 90:
    print('A')
if 90 > score >= 80:
    print('B')
if 80 > score >= 60:
    print('C')
if 60 > score >= 0:
    print('D')
if score < 0 or score > 100:
    print("输入错误！")
