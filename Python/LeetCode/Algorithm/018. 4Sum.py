# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: 018. 4Sum.py
# @time: 2019/02/26 20:35:14
# @contact: lodgeinwh@gmail.com
# @version: 1.0


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n < 4:
            return []

        res, nums_dic = set(), {}
        nums.sort()
        for i in range(n):
            for j in range(i + 1, n):
                key = nums[i] + nums[j]
                if key not in nums_dic.keys():
                    nums_dic[key] = [(i, j)]
                else:
                    nums_dic[key].append((i, j))

        for i in range(n):
            for j in range(i + 1, n - 2):
                x = target - nums[i] - nums[j]
                if x in nums_dic:
                    for k in nums_dic[x]:
                        if k[0] > j:
                            res.add((nums[i], nums[j], nums[k[0]], nums[k[1]]))
        return [list(i) for i in res]
