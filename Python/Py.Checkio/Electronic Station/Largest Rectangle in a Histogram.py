# !/usr/bin/env python3
# -*- encoding: utf-8 -*-
# @Author: lodge
# @Contact: lodgeinwh@gmail.com
# @File: Largest Rectangle in a Histogram.py
# @Time: 2019/2/12 21:51
# @Software: PyCharm


def largest_histogram1(histogram):
    import itertools

    def splitz(iterable):
        key = (min(iterable), )
        return [list(g) for k, g in itertools.groupby(iterable, lambda x: x in key) if not k]

    n = len(histogram)
    m = min(histogram)
    result = n * m
    histogram_list = splitz(histogram)
    for h in histogram_list:
        if largest_histogram1(h) > result:
            result = largest_histogram1(h)
    return result


def largest_histogram(histogram):
    max_height = max(histogram)
    min_height = min(histogram)
    length = len(histogram)
    max_square = min_height * length
    for current_height in range(min_height + 1, max_height + 1):
        current_length = 0
        for current_position in range(length):
            if histogram[current_position] >= current_height:
                current_length += 1
                square = current_length * current_height
                if square > max_square:
                    max_square = square
            else:
                current_length = 0
    return max_square


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    print("Done! Go check it!")
