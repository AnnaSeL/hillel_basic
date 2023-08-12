""""Function that shift the list by N elements to the right or left"""
def shift(seq, n):
    if n < 0:
        n = abs(n) % len(seq)
        return seq[n:] + seq[:n]
    if n > 0:
        n = n % len(seq)
        return seq[-n:] + seq[0:-n]
    else:
        return seq


data = input("Enter the sequence: ")
num = int(input("Enter the number: "))
list_data = data.split()
res = shift(list_data, num)
print(res)
