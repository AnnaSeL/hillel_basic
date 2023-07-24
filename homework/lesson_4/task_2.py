def enter_num():
    num = []
    sum = 0
    product = 1
    max = 1
    counter = 0
    index = 0
    even = 0
    odd = 0
    while True:
        n = int(input("Введіть послідовність цілих невід'ємних чисел: "))
        if n == 0:
            break
        sum += n
        product *= n

        if n > max:
            max = n

        if n % 2 == 0:
            even += 1
        if n % 2 != 0:
            odd += 1

        num.append(n)

    aver = sum/len(num)
    sort = reversed(num)
    sec_max = 0
    for i in sort:
        if i < max:
            sec_max = i
            break

    amount = num.count(max)

    print(f"кількість введених чисел: {len(num)}")
    print(f"сума: {sum}")
    print(f"добуток: {product}")
    print(f"середнє арифметичне: {aver}")
    print(f"значення та порядковий номер найбільшого елемента: {max}, індекс - [{num.index(max)}]")
    print(f"кількість парних - {even} та непарних елементів - {odd}")
    print(f"другий за величиною елемента: {sec_max}")
    print(f"кількість елементів послідовності,що дорівнюють її найбільшому елементу: {amount}")

enter_num()
