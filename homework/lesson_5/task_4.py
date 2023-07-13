def change(num):
    num = list(map(int, num))
    counter = 0
    for index, i in enumerate(num):
        if i % 2 != 0:
            num[index] = 0
            counter += 1
    print(num)
    print(f"Amount of odd numbers: {counter}")


num = input("Enter numbers: ")
num = num.split(' ')
change(num)
