# !/usr/bin/env python3
# -*- coding: utf-8 -*-


"""---第一个小游戏升级版---"""

import random

secret = random.randint(1, 10)
temp = input("不妨猜一下我现在心里想的数字：")
guess = int(temp)

while guess != secret:
    temp = input("哎呀，猜错了，再猜一次：")
    guess = int(temp)

    if guess == secret:
        print("你是我心里的蛔虫吗？")
        print("猜中了也没奖！")
    else:
        if guess > secret:
            print("哥，大了大了~~~")
        else:
            print("嘿嘿，小了小了~~~")

print("游戏结束！")
