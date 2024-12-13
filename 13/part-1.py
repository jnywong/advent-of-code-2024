import re
import math


def determinant(a, b, c, d):
    return a * d - b * c


data = []
with open("input.txt", "r") as file:
    for line in file:
        line = line.split()
        if line == []:
            continue
        else:
            data.append(line)

A = []
b = []
for i in range(len(data) // 3):
    A1 = int(re.findall(r"\d+", data[3 * i][2])[0])
    A2 = int(re.findall(r"\d+", data[3 * i + 1][2])[0])
    A3 = int(re.findall(r"\d+", data[3 * i][3])[0])
    A4 = int(re.findall(r"\d+", data[3 * i + 1][3])[0])
    A.append([[A1, A2], [A3, A4]])

    b1 = int(re.findall(r"\d+", data[3 * i + 2][1])[0])
    b2 = int(re.findall(r"\d+", data[3 * i + 2][2])[0])
    b.append([b1, b2])

press = []
for A_, b_ in zip(A, b):
    d = determinant(A_[0][0], A_[0][1], A_[1][0], A_[1][1])
    x1 = determinant(b_[0], A_[0][1], b_[1], A_[1][1]) / d
    x2 = determinant(A_[0][0], b_[0], A_[1][0], b_[1]) / d
    if all([x % 1 == 0 for x in (x1, x2)]):
        press.append([x1, x2])

tokens = sum([int(press[i][0] * 3 + press[i][1]) for i in range(len(press))])
print(f"{tokens = }")
