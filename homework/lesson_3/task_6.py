input("Введіть координати стартової та кінцевої клітини:")
x1 = int(input("x1 = "))
x2 = int(input("y1 = "))
y1 = int(input("x2 = "))
y2 = int(input("y2 = "))
dx = abs(x1-x2)
dy = abs(y1-y2)
if dx == 1 and dy == 2 or dx == 2 and dy == 1:
    print("Може потрапити.")
else:
    print("Не може потрапити.")

