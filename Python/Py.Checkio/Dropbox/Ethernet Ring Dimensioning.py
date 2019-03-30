# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: lodge
# @license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
# @contact: lodgeinwh@gmail.com
# @file: Ethernet Ring Dimensioning.py
# @time: 2019/1/5 18:43


ETHERNET = (100, 40, 10, 1, 0.1)  # Ethernet bandwidth capacity in Gbps


def checkio(ring, *flows):
    ring_temp = ring + ring[0]
    ring_map = []
    for i in range(len(ring_temp) - 1):
        ring_map.append(ring_temp[i:i + 2])

    count = []
    for i in range(len(ring_map)):
        count.append(0)

    for item in flows:
        start = ring.find(item[0][0])
        end = ring.find(item[0][-1])
        if start < end:
            if end - start > len(ring) // 2:
                for i in range(end, len(ring)):
                    count[i] += item[1]
                for i in range(start):
                    count[i] += item[1]
            else:
                for i in range(start, end):
                    count[i] += item[1]
        else:
            if start - end >= len(ring) // 2:
                for i in range(start, len(ring)):
                    count[i] += item[1]
                for i in range(end):
                    count[i] += item[1]
            else:
                for i in range(end, start):
                    count[i] += item[1]

    import math
    result = [0, 0, 0, 0, 0]
    for i in count:
        if i > max(ETHERNET):
            result[0] += int(i // 100) + math.ceil(i % 100 / 100)
        elif max(ETHERNET) > i > min(ETHERNET):
            n = 0
            while ETHERNET[n] >= i:
                n += 1
            result[n - 1] += 1
        elif min(ETHERNET) > i > 0:
            result[-1] += 1
    return result


if __name__ == '__main__':
    # These "asserts" are used only for self-checking and not necessary for auto-testing
    assert checkio("AEFCBG", ("AC", 5), ("EC", 10), ("AB", 60)) == [2, 2, 1, 0, 0]
    assert checkio("ABCDEFGH", ("AD", 4)) == [0, 0, 3, 0, 0]
    assert checkio("ABCDEFGH", ("AD", 4), ("EA", 41)) == [4, 0, 3, 0, 0]
