#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
from turtle import *
colormode(255)
left(45)
fd(100)
right(135)
fd(150)
left(135)
fd(100)
done()
'''


import turtle
turtle.setup(650, 350, 200, 200)
turtle.pu()
turtle.fd(-250)
turtle.pd()
turtle.width(25)
turtle.pencolor('purple')
turtle.seth(-40)
for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80 / 2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2 / 3)
turtle.done()
