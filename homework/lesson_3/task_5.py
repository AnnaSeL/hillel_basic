import random
for round in range(3):
    num = input('Введіть число від 1 до 10: ')
    rand = random.random()
    if int(num) == rand:
        print('You won :)')
        break
    else:
        print('You lose :(')
