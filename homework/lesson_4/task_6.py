def count():
    n = input("Введіть список чисел: ")
    num = n.split(' ')
    num = list(map(int, num))
    counter = 0
    for i in range(1,len(num)-2,1):
        if num[i]>num[i-1] and num[i]>num[i+1]:
            counter += 1
    print(counter)


count()
