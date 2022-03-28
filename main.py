# ！python3
# coding=utf8
"""
Author: 宋加运
Date: 2022/3/2 22:09
"""

from turtle import *
import random
import time

n = 0
needles = []  # 存储所有针
speed(0)


class Needles:
    """ 存储每一根针的长度和角度 """
    def __init__(self, length, angle):
        self.length = 200
        self.angle = 180


def draw_a_circle(c):
    """
    draw_a_circle: 画一个特定大小和颜色的填充圆
    param c: 圆的填充颜色
    """
    penup()
    goto(0, -100)
    setheading(0)
    fillcolor(c)
    begin_fill()
    circle(100)
    end_fill()
    penup()


def draw_a_needle():
    """ 画出固定于面板左侧的针发射位置 """
    penup()
    goto(-360, 0)
    pensize(5)
    pencolor('purple')
    pendown()
    goto(-295, 0)
    pensize(5)
    pencolor('orange')
    goto(-270, 0)
    penup()


def spin_needles():
    """ 实时更新每一个针的角度，长度不用改变 """
    global needles
    global n
    i = 0
    for i in range(n):
        needles[i].angle = needles[i].angle+1


def draw_needles():
    """ 根据插上去之后的每一根针的角度从而将其画出 """
    global needles
    global n
    i = 0
    for i in range(n):
        penup()
        goto(0, 0)
        setheading(needles[i].angle)
        pensize(3)
        pencolor("green")
        pendown()
        forward(100)
        pencolor("orange")
        forward(100)
        penup()


def new_needle():
    """ 随机发射出一根针 """
    global n
    a = random.randint(0, 100)
    if a < 4:
        newneedle = Needles(200, 180)
        needles.append(newneedle)  # 把新针加入列表
        n = n + 1


def stop():
    """
    判断新插入的针是否和已有的针插在一起（这里指角度相差小于2度），
    若插在一起则圆盘变红，程序结束
    """
    global n
    global needles
    for i in range(n):
        if abs(n-1-i) > 0 and abs(needles[n-1].angle - needles[i].angle) < 2:
            draw_a_circle('red')  # 圆盘变成红色
            time.sleep(3)
            exitonclick()


def main():
    hideturtle()
    speed(0)
    draw_a_circle('green')
    draw_a_needle()
    for r in range(0, 360 * 100, 3):
        tracer(False)
        clear()
        new_needle()
        spin_needles()
        draw_a_circle('green')
        draw_a_needle()
        draw_needles()
        time.sleep(0.01)
        tracer(True)
        stop()
    mainloop()


if __name__ == "__main__":
    main()
