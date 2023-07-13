def calculate(phrase):
    words = phrase.split(' ')
    symb = list(phrase)
    print(f"Amount of words: {len(words)}")
    print(f"Amount of symbols: {len(symb)}")


phrase = input("Enter your phrase: ")
calculate(phrase)
