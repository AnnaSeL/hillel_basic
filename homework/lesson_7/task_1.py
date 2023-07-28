def calculate(set1, set2):
    """Calculate the length of given sets"""
    return len(set1), len(set2)


set1 = set(input("Enter first set: ").split(' '))
set2 = set(input("Enter second set: ").split(' '))
res1, res2 = calculate(set1, set2)
print(f"Length of the first set and the second set: {res1}\n"
      f"Length of the second set: {res2}")
