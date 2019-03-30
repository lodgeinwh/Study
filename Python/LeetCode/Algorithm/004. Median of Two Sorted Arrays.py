# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: 004.4. Median of Two Sorted Arrays.py
# @time: 2019/02/26 20:30:21
# @contact: lodgeinwh@gmail.com
# @version: 1.0


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        merged = sorted(nums1 + nums2)
        size = len(merged)
        return merged[size // 2] if size % 2 else (
            merged[size // 2] + merged[size // 2 - 1]) / 2
