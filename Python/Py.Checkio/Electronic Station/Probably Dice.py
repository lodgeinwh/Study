# !/usr/bin/env python3
# -*- encoding: utf-8 -*-
# @Author: lodge
# @Contact: lodgeinwh@gmail.com
# @File: Probably Dice.py
# @Time: 2019/2/12 0:06
# @Software: PyCharm


def probability(dice_number, sides, target):
    if target < dice_number or target > dice_number * sides:
        return 0

    res = [[1] * sides]
    for i in range(1, dice_number):
        x = (sides - 1) * (i + 1) + 1
        res.append([0] * x)

        for j in range(x):
            if j < sides:
                res[i][j] = (sum(res[i - 1][0:j + 1]))
            elif sides <= j <= x // 2:
                res[i][j] = (sum(res[i - 1][j - sides + 1:j + 1]))
            else:
                break
        left = 0
        right = len(res[i]) - 1
        while left <= right:
            res[i][right] = res[i][left]
            left += 1
            right -= 1

    result = res[-1]
    all = sum(result)
    other = []
    for i, item in enumerate(result):
        pro = item / all
        other.append([dice_number + i, pro])

    return round(other[target - dice_number][1], 4)


if __name__ == '__main__':
    # These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision


    assert (almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    assert (almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    assert (almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    assert (almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    assert (almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    assert (almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    assert (almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"
