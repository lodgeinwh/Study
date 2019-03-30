# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: lodge
# @license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
# @contact: lodgeinwh@gmail.com
# @file: IP Network Route Summarization.py
# @time: 2019/1/5 18:43


def checkio(data):
    data_bin = []
    for ip in data:
        ip = ip.split('.')
        ip_bin = []
        for num in ip:
            num_bin = bin(int(num))[2:].zfill(8)
            ip_bin.append(num_bin)
        ip_str = ''.join(ip_bin)
        data_bin.append(ip_str)

    n = 1
    while all(ip.startswith(data_bin[0][:n]) for ip in data_bin):
        n += 1

    new_ip_bin = data_bin[0][:n - 1] + '0' * (len(data_bin[0]) - n + 1)

    return '{}.{}.{}.{}/{}'.format(int(new_ip_bin[0:8], base=2), int(new_ip_bin[8:16], base=2),
                                   int(new_ip_bin[16:24], base=2), int(new_ip_bin[24:32], base=2), n - 1)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"]) == "172.16.12.0/22"), "First Test"
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9"]) == "172.0.0.0/8"), "Second Test"
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9", "146.11.2.2"]) == "128.0.0.0/2"), "Third Test"
