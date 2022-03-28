from turtle import *
import keyboard
import time

n = 0
needles = []  # 存储所有针
speed(0)


class Needles:
    def __init__(self, length, angle):
        self.length = 200
        self.angle = 180


# 画一个绿色填充圆
def draw_a_circle():
    penup()
    goto(0, -120)
    setheading(0)
    fillcolor('green')
    begin_fill()
    circle(120)
    end_fill()
    penup()


def draw_a_needle():
    penup()
    goto(-360, 0)
    pensize(5)
    pencolor('purple')
    pendown()
    goto(-310, 0)
    pensize(5)
    pencolor('orange')
    goto(-290, 0)
    penup()


def key_down():
    global needles
    global n
    for r in range(0, 360 * 100, 3):
        tracer(False)
        if keyboard.read_key() == "space":
            newneedle = Needles(200, 180)
            needles.append(newneedle)  # 把新针加入列表中
            n = n+1
        time.sleep(0.01)
        tracer(True)


def spin_needles():
    global needles
    global n
    i = 0
    for i in range(n):
        needles[i].angle = needles[i].angle+1


def draw_needles():
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
        forward(120)
        pencolor("orange")
        forward(105)
        penup()


def draw():
    for r in range(0, 360 * 100, 3):
        tracer(False)
        clear()
        spin_needles()
        draw_a_circle()
        draw_a_needle()
        draw_needles()
        time.sleep(0.01)
        tracer(True)


def main():
    hideturtle()
    speed(0)
    draw_a_circle()
    draw_a_needle()
    tracer(False)  # 使多个绘制对象同时显示
    key_down()
    draw()
    tracer(True)
    mainloop()


if __name__ == "__main__":
    main()
