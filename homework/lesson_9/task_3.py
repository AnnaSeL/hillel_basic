"""Get the longest word in the phrase"""

text = input("Enter text: ")
sorted_text = sorted(text.split(), key=len, reverse=True)
print(f"The longest word: {sorted_text[0]}")

