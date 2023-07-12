x = float(input("Введіть x: "))
y = float(input("Введіть y: "))
res = x
day = 1
while res < y:
    day += 1
    res = res + res * 0.1
print("День " + str(day))

