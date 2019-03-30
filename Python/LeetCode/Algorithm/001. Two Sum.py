# !/usr/bin/env python3
# -*- encoding: utf-8 -*-
# @Author: Lodge
# @Contact: lodgeinwh@gmail.com
# @File: 001.Two Sum.py
# @Time: 2019/02/12 22:34:27


class Solution:
    def twosum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            x = nums[i]
            if target - x in dict:
                return [dict[target - x], i]
            dict[x] = i


s = Solution()
print(s.twosum([2, 7, 11, 15], 22))
