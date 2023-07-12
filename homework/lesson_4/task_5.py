n = input("Введіть рядок: ")
symb = list(n)
for index, value in enumerate(symb):
    if index == 2:
        print(f"третій символ: {value}")
    elif index == (len(n)-2):
        print(f"передостанній символ: {value}")
print("перші п'ять символів: ", end='')
for val in range(len(n)):
    if val < 5:
        print(symb[val], end='')
print("\nвесь рядок, крім двох останніх символів: ", end='')
for val in range(len(n)):
    if val < len(n)-2:
        print(symb[val], end='')
print("\nусі символи з парними індексами: ", end='')
for val in range(len(n)):
    if val % 2 == 0:
        print(symb[val], sep=' ', end='')
print("\nусі символи з непарними індексами: ", end='')
for val in range(len(n)):
    if val % 2 != 0:
        print(symb[val], sep=' ', end='')
print("\nусі символи у зворотному порядку: ", end='')
for val in range(len(n)-1, -1, -1):
    print(symb[val], sep=' ', end='')
print("\nусі символи рядка через один у зворотному порядку: ", end='')
for val in range(len(n)-1, -1, -2):
    print(symb[val], sep=' ', end='')
print(f"\nдовжина цього рядка: {len(n)}")
