"""Check if the given word is palindrom or not"""
# Паліндром — морд, ні лап
# Шалаш, зараз, Дід, Піп, 13231
def palindrom(word):
    word = word.replace(" ", "")
    word = word.replace(",", "")
    if len(word) < 1:
        return True
    if word[0] != word[-1]:
        return False
    return palindrom(word[1:-1])


word = input("Enter word: ")
print(palindrom(word.lower()))
