# !/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: Lodgeinwh
# @file: Network Attack.py
# @time: 2019/04/26 21:23:24
# @contact: lodgeinwh@gmail.com
# @version: 1.0


def capture(matrix):
    times = {}
    safed = []
    N = len(matrix)
    for i in range(N):
        times[i] = matrix[i][i]
        safed.append(False)
    safed[0] = True
    for i in range(1, N):
        if matrix[0][i] == 1 and safed[i] == False:
            safed[i] = True

    while sum(safed) != N:
        for i in range(1, N):
            if safed[i] == False:
                temp = []
                for j in range(1, N):
                    if matrix[i][j] == 1 and safed[j] == True:
                        temp.append([times[j], j])
                if temp != []:
                    times[i] += times[sorted(temp)[0][1]]
                    safed[i] = True
    return max(list(times.values()))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert capture([[0, 1, 0, 1, 0, 1], [1, 8, 1, 0, 0, 0], [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0], [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 8, "Base example"
    assert capture([[0, 1, 0, 1, 0, 1], [1, 1, 1, 0, 0, 0], [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0], [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 4, "Low security"
    assert capture([[0, 1, 1], [1, 9, 1], [1, 1, 9]]) == 9, "Small"
