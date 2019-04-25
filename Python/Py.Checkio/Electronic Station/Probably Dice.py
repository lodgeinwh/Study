# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: Probably Dice
# @time: 2019-02-12 9:47
# @contact: lodgeinwh@gmail.com


def probability(dice_number, sides, target):
    if target > dice_number * sides or target < dice_number:
        return 0

    result = [
        [1] * sides,
    ]
    for i in range(1, dice_number):
        x = (sides - 1) * (i + 1) + 1
        result.append([0] * x)

        for j in range(x):
            if j < sides:
                result[i][j] = (sum(result[i - 1][0:j + 1]))
            elif sides <= j <= x // 2:
                result[i][j] = (sum(result[i - 1][j - sides + 1:j + 1]))
            else:
                break
        left = 0
        right = len(result[i]) - 1
        while left <= right:
            result[i][right] = result[i][left]
            left += 1
            right -= 1

    res = result[-1]
    all = sum(res)
    other = []
    for i, item in enumerate(res):
        pro = item / all
        other.append([dice_number + i, pro])

    return round(other[target - dice_number][1], 4)


if __name__ == '__main__':
    # These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1**significant_digits
        return correct - precision < checked < correct + precision

    assert (almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    assert (almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    assert (almost_equal(probability(2, 6, 7),
                         0.1667)), "Maximum for two 6-sided dice"
    assert (almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    assert (almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    assert (almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    assert (almost_equal(probability(10, 10, 50),
                         0.0375)), "Many dice, many sides"
