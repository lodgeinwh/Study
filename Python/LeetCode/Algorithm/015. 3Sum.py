# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: 015. 3Sum.py
# @time: 2019/02/26 20:34:19
# @contact: lodgeinwh@gmail.com
# @version: 1.0


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        if n < 3:
            return []

        dict = {}
        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1

        pos, neg, rst, rsts = [], [], [], []
        dictkey = dict.keys()
        for k in dictkey:
            if k >= 0:
                pos.append(k)
            else:
                neg.append(k)

        if 0 in dictkey and dict[0] > 2:
            rsts.append([0, 0, 0])

        for p in pos:
            for n in neg:
                i = -(p + n)
                if i in dictkey:
                    if (i == p or i == n) and dict[i] > 1:
                        rst = [i, n, p]
                        rsts.append(sorted(rst))
                    elif i > p or i < n:
                        rst = [i, n, p]
                        rsts.append(rst)
        return rsts
