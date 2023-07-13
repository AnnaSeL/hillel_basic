import sys


def calc_area(h, a, par):
    if par == 1:
        area = 0.5 * h * a
        print(f"Triangle area = {area}")
    elif par == 2:
        area = a * a
        print(f"Square area = {area}")
    else:
        print("Incorrect value")
        sys.exit()


h = int(input("Enter the height: "))
a = int(input("Enter the base: "))
par = int(input("Area of which figure you want to find (1 - triangle, 2 - square): "))
calc_area(h, a, par)
