from openpyxl import *
from openpyxl.styles import PatternFill

wb = Workbook()
sheet = wb.create_sheet(index=0, title="NQueen")
n = 8
queenpos = [0 for i in range(100)]
answer_num = 0
queue = "♕"
row = [" ", " ", " ", " ", " ", " ", " ", " "]
row_num = 0

def bg_xlsx():
    black_fill = PatternFill(bgColor="000000", fill_type="solid")
    if row_num % 2 == 0:
        for i in range(n):
            if (i + 1) % 2 == 0:
                sheet.cell(row=row_num + 1, column=i + 1).fill = black_fill
    else:
        for i in range(n):
            if (i + 1) % 2 == 1:
                sheet.cell(row=row_num + 1, column=i + 1).fill = black_fill


def nqueen(k):
    global row_num
    global row
    global answer_num

    if k == n:
        for i in range(n):
            row_num = row_num + 1
            row[queenpos[i]] = "♕"
            sheet.append(row)
            print(queenpos[i] + 1)
        print("\n")
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


nqueen(0)
