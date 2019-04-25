#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: lodgeinwh
# @license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
# @contact: lodgeinwh@gmail.com
# @file: dict.py
# @time: 2018/10/21 18:16


def get_perator_name(number):
    number = int(number)
    for i in range(len(perator_dict)):
        if number in list(perator_dict.values())[i]:
            return list(perator_dict.keys())[i]


mobile = [134, 135, 136, 137, 138, 139, 147, 150, 151, 152, 157, 158, 159, 178, 182, 183, 184, 187, 188]
unicom = [130, 131, 132, 145, 155, 156, 171, 175, 176, 185, 186]
telecom = [133, 149, 153, 173, 177, 180, 181, 189, 199]
perator_num = [mobile, unicom, telecom]
perator_name = ['中国移动', '中国联通', '中国电信']
perator_dict = dict(zip(perator_name, perator_num))
num = input('请输入手机号码前三位：')
print(get_perator_name(num))
