num = input('Введіть десяткове число: ')
#fraction = float(num) - int(float(num)) #first option print("дрібну частину = " + str(round(fraction,2)))
fraction = round(float(num) % 1,2) #second option print("дрібну частину = " + str(fraction))
print("Дрібна частина = " + str(fraction))
for index, sym in enumerate(str(fraction)):
    if index == 2:
        print("Перша цифра після десяткової точки = " + sym)
        break
