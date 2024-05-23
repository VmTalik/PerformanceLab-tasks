import sys
from fractions import Fraction

file1_name = sys.argv[1]
file2_name = sys.argv[2]

with open(file1_name) as f:
    lines = f.readlines()
a, b = map(lambda i: Fraction(i), lines[0].split())  # координаты центра окружности
r = Fraction(lines[1])  # радиус окружности

with open(file2_name) as f:
    lines = f.readlines()
for line in lines:
    x, y = map(lambda i: Fraction(i), line.split())  # координаты точек
    if (x - a) ** 2 + (y - b) ** 2 == r ** 2:
        print(0)
    elif (x - a) ** 2 + (y - b) ** 2 < r ** 2:
        print(1)
    else:
        print(2)
