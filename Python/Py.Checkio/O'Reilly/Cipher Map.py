# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: Cipher Map.py
# @time: 2019/03/14 21:41:17
# @contact: lodgeinwh@gmail.com
# @version: 1.0


def recall_password(cipher_grille, ciphered_password):
    def rot(g):  # 定义一个转置函数
        return [[g[3 - y][x] for y in range(4)] for x in range(4)]

    password = []
    for i in range(4):
        password.extend([
            ciphered_password[x][y] for x in range(4) for y in range(4)
            if cipher_grille[x][y] == 'X'
        ])
        cipher_grille = rot(cipher_grille)
    return ''.join(password)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(('X...', '..X.', 'X..X', '....'),
                           ('itdf', 'gdce', 'aton',
                            'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(('....', 'X..X', '.X..', '...X'),
                           ('xhwc', 'rsqx', 'xqzz',
                            'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
