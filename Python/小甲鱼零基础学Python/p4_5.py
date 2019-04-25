#!/usr/bin/env python3
# -*- coding: utf-8 -*-


for i in range(10):
    if i % 2 != 0:
        print(i)
        continue
    i += 2
    print(i)
