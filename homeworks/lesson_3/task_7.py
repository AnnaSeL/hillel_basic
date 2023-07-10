num = input('Введіть число: ')
res = 1
for vari in range(int(num)):
    vari += 1
    res *= vari
print("factorial " + num + " = " + str(res))
