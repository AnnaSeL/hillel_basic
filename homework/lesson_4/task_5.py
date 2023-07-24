def get_symb():
    n = input("Введіть рядок: ")
    symb = list(n)
    third = symb[2]
    print(f"третій символ: {third}")
    pre_last = symb[-2]
    print(f"передостанній символ: {pre_last}")
    five = symb[0:5]
    print(f"перші п'ять символів: {five}")
    min_two = symb[0:len(symb)-2]
    print(f"весь рядок, крім двох останніх символів: {min_two}")
    even = symb[::2]
    print(f"усі символи з парними індексами: {even}")
    odd = symb[1::2]
    print(f"усі символи з непарними індексами: {odd}")
    back = symb[::-1]
    print(f"усі символи у зворотному порядку: {back}")
    back_one = symb[::-2]
    print(f"усі символи рядка через один у зворотному порядку: {back_one}")
    print(f"довжина цього рядка: {len(n)}")


get_symb()



