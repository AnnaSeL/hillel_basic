"""Function for changing words in the phrase"""
def replace_fun(phrase, word_to_replace, replace_word, repetition):
    return phrase.replace(word_to_replace, replace_word, int(repetition))


text = input("Enter text: ")
data = text.split('; ')
phrase = data[0]
word_to_replace = data[1]
replace_word = data[2]
repetition = data[3]
print(replace_fun(phrase, word_to_replace, replace_word, repetition))
