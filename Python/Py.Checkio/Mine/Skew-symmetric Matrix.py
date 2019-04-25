# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: Skew-symmetric Matrix.py
# @time: 2019/04/24 12:50:20
# @contact: lodgeinwh@gmail.com
# @version: 1.0


'''def checkio(matrix):
    import numpy as np
    trans_matrix = np.transpose(matrix)
    result = trans_matrix + matrix
    return all(j == 0 for i in result for j in i)'''


def checkio(matrix):
    return True if all(matrix[i][j] == -matrix[j][i] for i in range(len(matrix)) for j in range((len(matrix)))) else False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-2, -1, 0]]))

    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-2, -1, 0]]) == True, "1st example"
    assert checkio([
        [0, 1, 2],
        [-1, 1, 1],
        [-2, -1, 0]]) == False, "2nd example"
    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-3, -1, 0]]) == False, "3rd example"
    print("Coding complete? Click 'Check' to earn cool rewards!")
