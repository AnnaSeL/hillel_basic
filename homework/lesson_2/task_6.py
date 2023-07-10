x = float(input("Please enter a number: "))
given_list = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
i = 0
x = int(abs(x))
for num in given_list:
    if num == x:
        i += 1
        print("Your number is in the list!")
if i == 0:
    print("Your number isn't in the list")
