# !/usr/bin/env python3
# -*- encoding: utf-8 -*-
# @Author: lodge
# @Contact: lodgeinwh@gmail.com
# @File: 350. Intersection of Two Arrays II.py
# @Time: 2019/2/26 20:41
# @Software: PyCharm


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        result = []
        for s in nums2:
            if s in nums1:
                result.append(s)
                nums1.remove(s)
        return result
