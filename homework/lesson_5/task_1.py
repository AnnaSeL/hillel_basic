import sys


def is_prime(num):
    counter = 0
    for i in range(2, num // 2+1):
        if num % i == 0:
            counter += 1
    if counter == 0:
        print("True")
    else:
        print("False")


n = int(input("Введіть n: "))
if n < 0 or n > 1000:
    print("Incorrect value")
    sys.exit()
else:
    is_prime(n)

