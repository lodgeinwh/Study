# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: p4_2.py
# @time: 2019/03/14 22:49:07
# @contact: lodgeinwh@gmail.com
# @version: 1.0


score = int(input("请输入一个分数："))
if 100 >= score >= 90:
    print('A')
else:
    if 90 > score >= 80:
        print('B')
    else:
        if 80 > score >= 60:
            print('C')
        else:
            if 60 > score >= 0:
                print('D')
            else:
                if score < 0 or score > 100:
                    print("输入错误！")
