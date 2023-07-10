v = float(input("Введіть швидкість: "))
t = float(input("Введіть час: "))
if t > 10:
    print("Incorrect value. Try again! ")
    t = float(input("Введіть швидкість: "))
dist = round(v * t)
if dist < 0:
    flag = 100 + dist
    print("Вася зупиниться на позначці " + str(flag))
else:
    flag = 0 + dist
    if flag > 100:
        print("Вася зупиниться на позначці 100")
    else:
        print("Вася зупиниться на позначці " + str(flag))
