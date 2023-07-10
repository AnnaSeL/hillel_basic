year = int(input("Введіть рік: "))
if year % 4 == 0 and year % 100 != 0:
    print("YES")
elif year % 400 == 0:
    print("YES")
else:
    print("NO")
