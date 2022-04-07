# ！python3
# coding=utf8

n = 8
queenpos = [0 for i in range(100)]


def nqueen(k):
    if k == n:
        for i in range(n):

    for i in range(n):
        j = 0
        for j in range(k):
            if queenpos[j] == i or abs(queenpos[j] - i) == abs(k - j):
                break
        if j == k:
            queenpos[k] = i
            nqueen(k + 1)



