import math


def calculate(a):
    diag = round((a * math.sqrt(2)), 2)
    perim = 4 * a
    area = a * a
    res = diag, perim, area
    return res


a = int(input("Enter the side of a square: "))
res = calculate(a)
print(f"Diagonal = {res[0]}, perimetr = {res[1]}, area = {res[2]}")
