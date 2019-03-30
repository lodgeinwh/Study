# !/usr/bin/env python3
# -*- encoding: utf-8 -*-
# @Author: lodge
# @Contact: lodgeinwh@gmail.com
# @File: 217. Contains Duplicate.py
# @Time: 2019/2/26 20:39
# @Software: PyCharm


class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if nums == []:
            return False

        s = set(nums)
        return True if len(s) != len(nums) else False
