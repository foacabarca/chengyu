#!python3
# coding=utf8
"""
Project:送好友们的贺卡
Author:42024130-宋加运
Date:2022.4.10
"""
from docx import *
import openpyxl
import random
import time

wb = openpyxl.load_workbook("list.xlsx")
sh = wb.active
name_gender = []
ani = ["小兔子", "小老虎", "小麻雀", "孩子", "小猴子", "小松鼠"]
pic = ["flower.jpg", "fu.jpg", "rose.jpg", "zgj.jpg",
       "xnkl.jpg", "djdl.jpg", "xnkl1.jpg", "xnkl2.jpg", "xnkl3.jpg"]
word = ["天天开心！", "快快乐乐！", "开开心心！", "天天快乐！", "快乐开心！"]
for row in sh.rows:
    f = [c.value for c in row]
    name = f[0]
    gender = f[1]
    name_gender.append([name, gender])


def make_doc(name, gender):
    global pic
    global ani
    doc = Document()
    para = doc.add_paragraph(name)
    if gender == "男":
        para.add_run("先生：")
    else:
        para.add_run("女士：")
    para2 = doc.add_paragraph("         新的一年又来到，新的祝福也送到，祝你每天都能像")
    para2.add_run(ani[random.randint(0, 5)])
    para2.add_run("一样蹦蹦跳跳,")
    para2.add_run(word[random.randint(0, 4)])
    doc.add_picture(pic[random.randint(0, 8)])
    doc.save(f'{name}.docx')


for name, gender in name_gender:
    make_doc(name, gender)
    time.sleep(0.01)

