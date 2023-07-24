def grow():
    a = int(input("Введіть A: "))
    b = int(input("Введіть B: "))
    if a < b:
        for num in range(b-a+1):
            num += a
            print(num)
    elif a > b:
        for num in range(a-b+1):
            num -= a
            print(abs(num))


grow()
