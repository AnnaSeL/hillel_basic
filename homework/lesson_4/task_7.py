def print_num():
    n1 = input("Введіть список чисел 1: ")
    n2 = input("Введіть список чисел 2: ")
    num1 = n1.split(' ')
    num1 = list(map(int, num1))
    num2 = n2.split(' ')
    num2 = list(map(int, num2))
    counter1 = list(set(num1) & set(num2))
    counter2 = list(set(num1) - set(num2))
    counter3 = list((set(num1) - set(num2)) | (set(num2) - set(num1)))
    print(f"числа, що містяться одночасно як у першому списку, так і в другому: {counter1}")
    print(f"числа, що містяться в першому, але відсутні в другому: {counter2}")
    print(f"тільки унікальні для першого та другого списків: {counter3}")

print_num()
