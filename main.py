from openpyxl import *
from openpyxl.styles import Font
from openpyxl.styles import Alignment
from openpyxl.styles import PatternFill

wb = load_workbook("E:/PythonProject/nqueen.xlsx")
sheet = wb["Sheet1"]
n = 8  # 设置n皇后的皇后数目
queenpos = [0 for i in range(n)]
answer_num = 0  # n皇后解的个数
row_num = 0  # 行数
height = 35
width = 30
alignment = Alignment(horizontal="center", vertical="center", text_rotation=0, wrap_text=True)
font1 = Font(name="微软雅黑", size=20, bold=True, italic=False, color="000000")
font2 = Font(name="微软雅黑", size=20, bold=True, italic=False, color="FFFFFF")


def fillcolor0():
    global row_num
    global sheet
    global height
    global width
    sheet.row_dimensions[row_num + 1].height = height
    sheet.row_dimensions[row_num + 1].width = width
    for i in range(n):
        sheet.cell(row=row_num + 1, column=i + 1).fill = PatternFill(fgColor="20B2AA", fill_type="solid")


def fillcolor1():
    """
    奇数行：偶数列填充黑色，字体颜色为白色
    偶数行：奇数列填充黑色，字体颜色为白色
    其他单元格字体颜色为白色
    另外设置单元格的宽和高
    """
    global height, width, row_num, font1, font2, alignment, sheet
    sheet.row_dimensions[row_num + 1].height = height
    sheet.row_dimensions[row_num + 1].width = width
    for i in range(n):
        sheet.cell(row=row_num + 1, column=i + 1).alignment = alignment
        if row_num % 2 == (i + 1) % 2:
            sheet.cell(row=row_num + 1, column=i + 1).fill = PatternFill(fgColor="000000", fill_type="solid")
            sheet.cell(row=row_num + 1, column=i + 1).font = font2
        else:
            sheet.cell(row=row_num + 1, column=i + 1).font = font1


def nqueen(k):
    global row_num, answer_num, queenpos, n
    if k == n:
        for i in range(n):
            row = ["" for l in range(n)]
            row[queenpos[i]] = "♕"
            sheet.append(row)
            fillcolor1()
            row_num = row_num + 1
        sheet.append(["" for l in range(n)])
        fillcolor0()
        answer_num = answer_num + 1
        row_num = row_num + 1
        return
    for i in range(n):
        j = 0
        while j < k:
            if queenpos[j] == i or abs(queenpos[j] - i) == abs(k - j):
                break
            j = j + 1
        if j == k:
            queenpos[k] = i
            nqueen(k + 1)
    print(answer_num)


nqueen(0)
wb.save("E:/PythonProject/nqueen.xlsx")
